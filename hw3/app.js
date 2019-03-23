$(document).ready(function(){
    $("#root").append("<input id='add_task_input'>");
    $("#root").append("<button id='add_task'>ADD</button>");
    $("#root").append("<ul></ul>");

    $("#add_task").click(function(){
        var txt = "Idle";
        if($("#add_task_input").val() !== "") {
            txt = $("#add_task_input").val();
        }
        var new_li = document.createElement("li");
        new_li.innerHTML = "<span>"+txt+"</span>"+"<button onclick='this.parentNode.remove()'>Delete</button>";
        $("ul").append(new_li);
    });
});
