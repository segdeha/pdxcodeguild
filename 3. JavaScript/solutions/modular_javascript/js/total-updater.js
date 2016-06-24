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

    function calculateCost(costs, numberOfExtras, isBeingDelivered) {
        var baseCost = 6;
        var extraCost = 0;
        var deliveryCost = 0;

        // Get extraCost value
        extraCost = costs['extra-ingredients'] * numberOfExtras;

        // Get deliveryCost value
        if (isBeingDelivered){
            deliveryCost = costs['delivery'];
        }

        return (baseCost + extraCost + deliveryCost).toFixed(2);
    }
    function updateTotal(form, output, costs) {
        var numberOfExtras   = form.querySelectorAll('.checked [name=extra-ingredients]').length;
        var isBeingDelivered = (form.elements.delivery.value === 'delivery');
        var totalCost        = calculateCost(costs, numberOfExtras, isBeingDelivered);

        output.innerHTML = `<strong>Total:</strong> $${totalCost}`;
    }
    return {
        updateTotal: updateTotal,
        calculateCost: calculateCost
    };
});
