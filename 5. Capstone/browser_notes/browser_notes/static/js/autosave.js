




$('.ui.button').on('click', function() {
        var note_id = $('#current-note').attr('data-id');
        var note = $('#current-note').html();
        $.post({
            url: '/notes/',
            data: {
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val(),
                note_id: note_id,
                note: note


            },

            success: function (data) {
                console.log(data)
                $('#current-note').attr('data-id', data.id);
                updateList();
            }
        });
    });



function updateList() {
    console.log("updatelist")
    $.ajax({
        url: '/notes/',
        success: function (data) {
            console.log(data)
                $('#notes-list').html(data);
            }

    })

}

