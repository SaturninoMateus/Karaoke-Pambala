/**
 * Created by theoneid on 01/12/15.
 */


function comentar(usuario, id, token){
    var id2 = usuario+'input'+id;
    var comentario = document.getElementById(id2).value;
    //Flag, 0 = comentario, 1 = curtir
    var flag = 0;
    param = {"comentario":comentario,"id":id, "csrfmiddlewaretoken":token, "usuario":usuario, "id":id, "flag":flag};

    if (comentario.length > 0){
         $.ajax({
        type: "POST",/*method type*/
        url: "/feed/",/*Target function that will be return result*/
        data: param,/*parameter pass data is parameter name param is value */
        dataType: "json",
        success: function(data) {
               alert("Success");
            }

    });
        location.reload();
    }


}

function curtir(usuario, id, token){
    /*Flag, 0 = comentario, 1 = curtir*/
    var flag = 1;
    param = {"id":id, "csrfmiddlewaretoken":token, "usuario":usuario, "id":id, "flag":flag};

    $.ajax({
        type: "POST",/*method type*/
        url: "/feed/",/*Target function that will be return result*/
        data: param,/*parameter pass data is parameter name param is value */
        dataType: "json",
        success: function(data) {
               alert("Success");
            }

    });
    location.reload();

}