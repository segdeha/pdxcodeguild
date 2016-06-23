/**
 * Update a UI widget with the list of ingredients being ordered.
 * @desc Update the DOM element passed in to the `output` argument with HTML
 * structure in the following way:
 * <ul class="ui relaxed list">
 *     <li class="item">White Tortilla</li>
 *     <li class="item">Beans</li>
 *     <li class="item">Cheese</li>
 *     <li class="item">Salsa</li>
 *     <li class="item">Sour Cream</li>
 * </ul>
 * @param {DOM element} output Reference to the <ul></ul> DOM element in which
 *     to display the order details as <li></li> tags
 * @param {Object} costs Object literal containing data about the costs of
 * different items, formatted as follows:
 * {
 *     String: Number.<amount>,
 *     String: Number.<amount>,
 *     ...
 *     String: Number.<amount>
 * }
 * Where the key is a string that matches the `name` attribute of a field or
 * fields (i.e. a set of checkboxes) and the value is the amount that thing
 * or each of those things cost.
 * @return {void}
 */
define(['./total-updater'], function (totalUpdater) {
    function thanks(output, costs) {
        var ingredients = [
            'tortilla',
            'meat',
            'included-ingredients',
            'extra-ingredients'
        ];

        var humanReadable = { // TODO expose this from a module to make things more DRY
            'white': 'White Flour Tortilla', 'wheat': 'Wheat Flour Tortilla',
            'spinach': 'Spinach Tortilla', 'corn': 'Corn Tortilla (gluten-free)',
            'carnitas': 'Carnitas', 'chicken': 'Chicken', 'sofritas': 'Sofritas (tofu)',
            'beans': 'Beans', 'cheese': 'Cheese', 'salsa': 'Salsa', 'sour cream': 'Sour Cream',
            'guacamole': 'Guacamole', 'scrambled-egg': 'Scrambled Egg', 'potatoes': 'Home Fried Potatoes',
            'sun-dried-tomatoes': 'Sun-dried Tomatoes', 'olives': 'Olives',
            'sauteed-mushrooms': 'Sautéed Mushrooms', 'sauteed-onions': 'Sautéed Onions',
            'jalapenos': 'Jalapeño Peppers'
        };

        // TODO expose this from a module
        // parse the browser's query string
        // based on: http://stackoverflow.com/a/3855394/11577
        // (but changed to handle multiple instances any particular name)
        var qs = (function(nvps) { // nvps == name value pairs
            if (nvps === '') {
                return null;
            }
            var rzlt = {};
            var rgxp = /\+/g;
            nvps.forEach(function (nvp) {
                var pair = nvp.split('=', 2); // limit to 2 items
                if (pair.length > 1) {
                    // if the key already exists, make the values into an array
                    if (rzlt[pair[0]]) {
                        // if it's ready an array, just add the new value
                        if (Array.isArray(rzlt[pair[0]])) {
                            rzlt[pair[0]].push(pair[1]);
                        }
                        // convert the value into an array and add the new value
                        else {
                            rzlt[pair[0]] = [
                                rzlt[pair[0]],
                                pair[1]
                            ];
                        }
                    }
                    // create a new key
                    else {
                        rzlt[pair[0]] = decodeURIComponent(pair[1].replace(rgxp, ' '));
                    }
                }
            });
            return rzlt;
        })(window.location.search.substr(1).split('&'));

        var lis  = [];
        for (var key in qs) {
            if (ingredients.indexOf(key) > -1) {
                if (Array.isArray(qs[key])) {
                    qs[key].forEach(function (value) {
                        lis.push(`<li class="item">${humanReadable[value]}</li>`);
                    });
                }
                else {
                    lis.push(`<li class="item">${humanReadable[qs[key]]}</li>`);
                }
            }
        }

        var costs            = { 'extra-ingredients': 0.5, 'delivery': 5 }; // TODO expose this from a module to make things more DRY
        var numberOfExtras   = qs['extra-ingredients'] ? qs['extra-ingredients'].length : 0;
        var isBeingDelivered = qs['delivery'] === 'delivery';

        var totalCost        = totalUpdater.calculateCost(costs, numberOfExtras, isBeingDelivered);
        var deliveryOption   = isBeingDelivered ? 'delivery' : 'in-store pick-up';

        if (lis.length > 0) {
            var html = `
                <ul class="ui relaxed list">
                    ${lis.join('')}
                </ul>
                <p>
                    Your order is set for <strong>${deliveryOption}.</strong>
                </p>
                <h3 class="ui block header">
                    Total Cost: $${totalCost}
                </h3>
            `;

            output.innerHTML = html;
        }
    }
    return thanks;
});
