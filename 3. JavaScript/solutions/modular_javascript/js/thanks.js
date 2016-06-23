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
define(function () {
    // based on: http://stackoverflow.com/a/3855394/11577
    var qs = (function(a) {
        if (a === '') return null;
        var b = {};
        var r = /\+/g;
        for (var i = 0; i < a.length; i += 1) {
            var p = a[i].split('=', 2);
            if (p.length === 1) {
                b[p[0]] = '';
            }
            else {
                b[p[0]] = decodeURIComponent(p[1].replace(r, ' '));
            }
        }
        return b;
    })(window.location.search.substr(1).split('&'));

    function thanks(output, costs) {
    }
    return thanks;
});
