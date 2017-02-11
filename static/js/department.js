/**
 * Created by zhangli on 2017/1/28.
 */


var manager_id = $('#manager').data('target');
if (manager_id != 'None'){
    $('#manager').val(manager_id);
}

var parent_id = $('#parent').data('target');
if (parent_id != ''){
    $('#parent').val(parent_id);
}



function delete_object(e) {
    var department_id = e.getAttribute('data-target');
    console.log(department_id);
    $.ajax({
        url: '/department/' + department_id + '/delete/',
        type: 'POST',
        data: {},
        success: function (result) {
            if (result.code == 0){
                window.location = '/department';
            }else{
                alert(result.message);
            }
        }
    });
}