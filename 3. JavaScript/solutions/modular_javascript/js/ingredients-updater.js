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
 * @param {DOM element} form Reference to the DOM element for the <form></form>
 * @param {DOM element} output Reference to the <ul></ul> DOM element in which
 *     to display the ingredients as <li></li> tags
 * @param {Array.<string>} ingredients Array of names of the ingredients
 * @return {void}
 */
define(function () {
    function updateIngredients(form, output, ingredients) {
        // do your work here
        var selectors = []; //make an array of CHECKED values
        ingredients.forEach(function(value) {
            var selector = '.checked [name=' + value + ']';// loop over the CHECKED boxes
            selectors.push(selector); //push the checked items into selctors array
        });

        var nodes = document.querySelectorAll(selectors.join(', ')); // join the CHECKED values with commas
        nodes = Array.prototype.slice.call(nodes); // turns the nodes variable into an array in a snap!
        var humanReadable = {
            //Tortillas
            'white': 'White Flour', 'wheat': 'Wheat Flour', 'spinach': 'Spinach', 'corn': 'Corn (gluten-free)',
            //Meat
            'carnitas': 'Carnitas', 'chicken': 'Chicken', 'sofritas': 'Sofritas (tofu)',
            //Included
            'beans': 'Beans', 'cheese': 'Cheese', 'salsa': 'Salsa', 'sour cream': 'Sour Cream',
            //Extras
            'guacamole': 'Guacamole', 'scrambled-egg': 'Scrambled Egg', 'potatoes': 'Home Fried Potatoes',
            'sun-dried-tomatoes': 'Sun-dried Tomatoes', 'olives': 'Olives', 'sauteed-mushrooms': 'Sautéed Mushrooms',
            'sauteed-onions': 'Sautéed Onions', 'jalapenos': 'Jalapeño Peppers'
        };

        var lis = []; // create array to push innerHTML to.
        nodes.forEach(function (node) { // loop over ingredients array
            lis.push('<li class="item">' + humanReadable[node.value] +  '</li>'); // push each ingredient onto lis
        });

        var html = '<ul class="ui relaxed list">' + lis.join('') + '</ul>'; // make a string
        output.innerHTML = html; // send the string to html
    }
    return updateIngredients;
});
