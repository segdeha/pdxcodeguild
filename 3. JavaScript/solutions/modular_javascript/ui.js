// initialize semantic-ui checkboxes and radio buttons
$('.ui.checkbox').checkbox()

// prevent the form from submitting when the user hits the submit button
document.querySelector('form').addEventListener('submit', function (evt) {
    evt.preventDefault();
})
