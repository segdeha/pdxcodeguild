requirejs(
    ['./jquery', './semantic', './ingredients-updater', './total-updater', './validator'],
    function ($, semantic, updateIngredients, updateTotal, validate) {

    // initialize semantic-ui checkboxes and radio buttons
    $('.ui.checkbox').checkbox()

    var form = document.querySelector('form');

    form.addEventListener('change', function (evt) {
        updateTotal();
        updateIngredients();
    });

    form.addEventListener('submit', function (evt) {
        // prevent the form from submitting when the user hits the submit button
        evt.preventDefault();
        validate();
    });
});
