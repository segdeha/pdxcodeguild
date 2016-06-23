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
<<<<<<< HEAD
    function updateTotal(form, output, costs) {
      // Setup
      // ----------------------
        // Cost Variables
      var baseCost = 6;
      var extraCost = 0;
      var deliveryCost = 0;
      var totalCost = 0;
      var perItemCost = costs['extra-ingredients']; // .50

        // Node List
      var checked = form.querySelectorAll('.checked [name=extra-ingredients]')

        // DOM Node
      var deliveryNode = form.querySelector('[name=delivery]');
=======
    function calculateCost(costs, numberOfExtras, isBeingDelivered) {
        var baseCost = 6;
        var extraCost = 0;
        var deliveryCost = 0;
>>>>>>> master

        // Get extraCost value
        extraCost = costs['extra-ingredients'] * numberOfExtras;

        // Get deliveryCost value
<<<<<<< HEAD
      if (form.elements.delivery.value === 'delivery'){
          deliveryCost = costs['delivery'];
      }
=======
        if (isBeingDelivered){
            extraCost += costs['delivery'];
        }
>>>>>>> master

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
