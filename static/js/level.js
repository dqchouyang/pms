/**
 * Created by zhangli on 2017/2/11.
 */


var level_id = $('#level').data('target');
if (level_id != 'None'){
    $('#level').val(level_id);
}

var user_id = $('#user').data('target');
if (user_id != ''){
    $('#user').val(user_id);
}


function delete_level(e) {
    var level_id = e.getAttribute('data-target');
    $.ajax({
        url: 'level/' + level_id + '/delete/',
        type: 'POST',
        data: {},
        success: function (result) {
            if (result.code == 0){
                window.location = '/reward/level';
            }else{
                alert(result.message);
            }
        }
    });
}


function delete_punish(e) {
    var punish_id = e.getAttribute('data-target');
    $.ajax({
        url: 'punish/' + punish_id + '/delete/',
        type: 'POST',
        data: {},
        success: function (result) {
            if (result.code == 0){
                window.location = '/reward/punish';
            }else{
                alert(result.message);
            }
        }
    });
}