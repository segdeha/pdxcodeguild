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

    var selectors = [];
      selector.push(selector);

    ingredients.forEach(function(value) {
      var selector = '.checked [name= ' + value + ']';

        var nodes = document.querySelectorAll(selectors.join(','));

      console.log(nodes)

    });



        // alert('updateIngredients');
    }
    return updateIngredients;
});
