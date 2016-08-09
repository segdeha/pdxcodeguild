


// jQuery to update list after autosave and editing.


function updateList() {
    console.log("updatelist")
    $.ajax({
        url: '/notes/',
        success: function (data) {

                $('#notes-list').html(data);
            }

    })

}

// jQuery will run when the page loads for autosave.
//

$(function(){
    // on key up autosave is initiated
    // we listening to the current-note element
    var $current_note = $('#current-note');
    $current_note.on('keyup', function(){
        console.log("keyup fired")
        $(this).off('keyup'); // turns off on keyup event listener.
        var interval = 1000 * 5;  // interval of 15 seconds between saves.
        setInterval(function () {
            console.log("about to save")
            var note_id = $current_note.attr('data-id');
            var note = $current_note.val();
            console.log(note)
            $.post({
                url: '/notes/',
                data: {
                    csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val(),
                    note_id: note_id,
                    note: note


                },

                success: function (data) {
                    console.log("successfully saved")
                    $current_note.attr('data-id', data.id);
                    updateList();    // call update list function
                }
            });

        }, interval )
    })

});



// jQuery to load note_id into current-note div


$("#notes-list").on('click', function(evt) {
  var note_id = $(evt.target).attr('data-id');
    // console.log(note_id)
  $.ajax({
      type: "GET",
      url: "/note",
      data: {csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val(),
                    note_id: note_id},

      success: function (data) {

          $('#current-note').attr('data-id', note_id).val(data.note);
      }
  });


});
