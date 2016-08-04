 $('.ui.button').on('click', function() {
        var note_id = $('#current-note').html();
        $.post({
            url: '//localhost:8000/notes/',
            data: {
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val(),
                note: note_id
            },

                    success: function (data) {
                $('#notes-list').html(data);
            }
        });
    });

            



