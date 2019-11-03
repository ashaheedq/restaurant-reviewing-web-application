function openEditForm(elt) {
    var key = elt.parentNode.parentNode.id;

    // Get the modal
    var modal = document.getElementById("myModal");

    // Get the form
    var form = document.getElementById("form1");

    // Get form header
    var formHeader = document.getElementById("form-header");

    // Get row data
    var row = document.getElementById(key);

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // update form title
    formHeader.textContent = "Edit this record";

    // update fields
    for (var i = 0; i < form.length - 1; i++) {
        form.elements[i].value = row.children[i].textContent;
    }
    modal.style.display = "block";

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
}

function openInsertForm() {
    // Get the modal
    var modal = document.getElementById("myModal");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // Get the form
    var form = document.getElementById("form1");

    // Get form header
    var formHeader = document.getElementById("form-header");

    formHeader.textContent = "Create a new record";
    for (var i = 0; i < form.length - 1; i++) {
        form.elements[i].value = ""
    }
    modal.style.display = "block";

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    };

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
}