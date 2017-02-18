var emp_id = $('#emp').data('target');
console.log(emp_id);
if (emp_id != 'None'){
    $('#emp').val(emp_id);
}


function delete_salary(e){
    var salary_id = e.getAttribute('data-target');
    $.ajax({
        url: 'salary/' + salary_id + '/delete/',
        type: 'POST',
        data: {},
        success: function (result) {
            if (result.code == 0){
                window.location = '/salary';
            }else{
                alert(result.message);
            }
        }
    });
}