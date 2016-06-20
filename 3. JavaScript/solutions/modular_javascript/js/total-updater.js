/**
 * Update a UI widget with the total cost of the item being ordered.
 * Total dollar amount should be displayed in U.S. Dollars.
 * @param {DOM element} form Reference to the DOM element for the <form></form>
 * @param {DOM element} output Reference to the DOM element in which to display
 *     the total price
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
    function updateTotal(form, output, costs) {
        // do your work here
        // alert('updateTotal');
    }
    return updateTotal;
});
