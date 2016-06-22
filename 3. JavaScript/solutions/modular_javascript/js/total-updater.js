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
      // Setup
      // ----------------------
      // Cost Variables
      var baseCost = 6;
      var extraCost = 0;
      var deliveryCost = 0;
      var totalCost = 0;

      // DOM Nodes
      var extraIngredientsNode = form['extra-ingredients']
      var deliveryNode = form['delivery']
      // Remember output is passed to the function

      // Transform
      // ----------------------
      // Get extraCost value
      for (var i = 0; i < extraIngredientsNode.length; i ++ ){

          // Get DOMTokenList of Parent div and if checked add 0.5 to extraCost
          var node = extraIngredientsNode[i].parentNode.classList;
          var array = Array.prototype.slice.call(node);
          if (array.indexOf('checked') + 1 ){ // add one because 0 is valid.
            extraCost += costs['extra-ingredients'];
          }

      }

      // Get deliveryCost value
      if (deliveryNode.value == 'delivery'){
          extraCost += costs['delivery'];
      }

      // output
      totalCost = baseCost + extraCost + deliveryCost;
      output.innerHTML = `<strong>Total:</strong> $${totalCost.toFixed(2)}`;

    }
    return updateTotal;
});
