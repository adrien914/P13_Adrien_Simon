 function autocomplete(inp, arr) {
     /*the autocomplete function takes two arguments,
     the text field element and an array of possible autocompleted values:*/
     var currentFocus;
     /*execute a function when someone writes in the text field:*/
     var a, b, i, val = inp.value;
     /*close any already open lists of autocompleted values*/
     closeAllLists();
     if (!val) {
         return false;
     }
     currentFocus = -1;
     /*create a DIV element that will contain the items (values):*/
     a = document.createElement("DIV");
     a.setAttribute("id", this.id + "autocomplete-list");
     a.setAttribute("class", "autocomplete-items");
     /*append the DIV element as a child of the autocomplete container:*/
     inp.parentNode.appendChild(a);
     /*for each item in the array...*/
     console.log(arr)
     for (i = 0; i < arr.length; i++) {
         console.log(arr[i])
         /*create a DIV element for each matching element:*/
         b = document.createElement("DIV");
         /*make the matching letters bold:*/
         b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
         b.innerHTML += arr[i].substr(val.length);
         /*insert a input field that will hold the current array item's value:*/
         b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
         /*execute a function when someone clicks on the item value (DIV element):*/
         b.addEventListener("click", function (e) {
             /*insert the value for the autocomplete text field:*/
             inp.value = this.getElementsByTagName("input")[0].value;
             $("#search_form").submit()
             /*close the list of autocompleted values,
             (or any other open lists of autocompleted values:*/
             closeAllLists();
         });
         a.appendChild(b);
     }
 }
  function closeAllLists() {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      x[i].parentNode.removeChild(x[i]);
  }
}
/*execute a function when someone clicks in the document:*/
document.addEventListener("click", function (e) {
    closeAllLists(e.target);
})

 $(document).ready(function() {
    $("#search_form").submit(function(event) {
        event.preventDefault()
        id = document.getElementById('search').value.split(':')[0]
        location.href = "/page_admin/" + id
    })
})

 function set_listener(csrf_token){
     console.log("étest")
    search_bar = document.getElementById('search')
    search_bar.addEventListener('input', function (evt) {
        text = search_bar.value
        $.ajax({
            type: "POST",
            url: "/search_engine/",
            data: {
                text: text,
                csrfmiddlewaretoken: csrf_token
            },
            success: function (data) {
                if (data.propositions.length <= 10 && data.propositions.length > 0)
                    autocomplete(search_bar, data.propositions)
                else {
                    closeAllLists()
                }
            }
        })
    });
 }