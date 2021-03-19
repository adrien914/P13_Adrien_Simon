function save(fiche_id, csrf_token) {
    const inputs = ["#image", "#nom", "#email", "#telephone", "#fax",
        "#rang_affichage", "#nombre_elements_ligne", "#pole", "#fonction", "#grade", "#groupe"]
    let data = {id: fiche_id, csrfmiddlewaretoken: csrf_token}
    /* For each input add its value to the key corresponding to his id without the # to data */
    inputs.forEach(function (id) {
        data[id.replace("#", "")] = $(id).val()
    })
    etat = $("#etat").is(":checked")
    if (etat) {
        data["etat"] = "pub"
    } else {
        data["etat"] = "not_pub"
    }
    $.ajax({
        url: "/modify_fiche/",
        type: "POST",
        data: data,
        success: function () {
            if (!fiche_id)
                location.reload()
            else
                toastr.success('Sauvegardé avec succès!')
        },
        error: function () {
            toastr.error('Erreur a la sauvegarde!')
        }
    })
}

function remove_fiche(fiche_id, csrf_token) {
    $.ajax({
        url: "/remove_fiche/",
        type: "POST",
        data: {fiche_id: fiche_id, csrfmiddlewaretoken: csrf_token},
        success: function () {
            location.href = "/page_admin/"
        },
        error: function () {
            toastr.error("Erreur a la suppression de la fiche")
        }
    })
}

function change_pole(new_pole) {
    document.getElementById("pole").value = new_pole
    $("#pole_modal").modal("hide")
}

function change_fonction(new_fonction) {
    document.getElementById("fonction").value = new_fonction
    $("#fonction_modal").modal("hide")
}

function change_groupe(new_groupe) {
    document.getElementById("groupe").value = new_groupe
    $("#groupe_modal").modal("hide")
}

function change_grade(new_grade) {
    document.getElementById("grade").value = new_grade
    $("#grade_modal").modal("hide")
}

function change_image(new_image) {
    document.getElementById("image").setAttribute("value", new_image)
    document.getElementById("image-img").setAttribute("src", "/media/" + new_image)
    $("#image_modal").modal("hide")
}

function add_fonction(csrf_token) {
    nom = $("#ajouter_fonction_input").val()
    $.ajax({
        url: "/add_fonction/",
        type: "POST",
        data: {nom: nom, csrfmiddlewaretoken: csrf_token},
        success: function () {
            toastr.success("Fonction ajoutée avec succès")
            change_fonction(nom)
        },
        error: function () {
            toastr.error('Erreur a la sauvegarde!')
        }
    })
}

function add_grade(csrf_token) {
    nom = $("#ajouter_grade_input").val()
    $.ajax({
        url: "/add_grade/",
        type: "POST",
        data: {nom: nom, csrfmiddlewaretoken: csrf_token},
        success: function () {
            toastr.success("Fonction ajoutée avec succès")
            change_grade(nom)
        },
        error: function () {
            toastr.error('Erreur a la sauvegarde!')
        }
    })
}

function add_groupe(csrf_token) {
    nom = $("#ajouter_groupe_input").val()
    importance = $("#ajouter_groupe_input_importance").val()
    $.ajax({
        url: "/add_groupe/",
        type: "POST",
        data: {nom: nom, importance: importance, csrfmiddlewaretoken: csrf_token},
        success: function () {
            toastr.success("Fonction ajoutée avec succès")
            change_groupe(nom)
        },
        error: function () {
            toastr.error('Erreur a la sauvegarde!')
        }
    })
}

function add_image(csrf_token) {
    var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            url: "/add_image/",
            type: "POST",
            contentType: false,
            cache: false,
            processData: false,
            data: form_data,
            success: function () {
                toastr.success("Fonction ajoutée avec succès")
                const image_fake_path = document.getElementById("image_input").value
                const image_name = image_fake_path.split("\\").pop()
                change_image("photos/" + image_name)
            },
            error: function () {
                toastr.error('Erreur a la sauvegarde!')
            }
        })
}

function reset(id) {

    document.getElementById(id).value = ""
}

function go_down_fiche(fiche_id, csrf_token) {
    const fiche = $("#fiche-" + fiche_id)
    console.log(fiche)
    const next_fiche = fiche.next()
    console.log(next_fiche.length)
    if (next_fiche.length) {
        const new_rank = next_fiche.data("rang") + 1
        fiche.insertAfter(next_fiche)
        $.ajax({
            url: "/change_rank/",
            type: "POST",
            data: {id: fiche_id, rank: new_rank, csrfmiddlewaretoken: csrf_token},
            success: function () {
                toastr.success('Nouveau rang sauvegardé avec succès')
            },
            error: function () {
                toastr.error('Erreur a la sauvegarde!')
            }
        })
    } else {
        toastr.warning("Ça se voit pas qu'il n'y a pas d'autre fiche ? :)")
    }
}

function go_up_fiche(fiche_id, csrf_token) {
    const fiche = $("#fiche-" + fiche_id)
    console.log(fiche)
    const previous_fiche = fiche.prev()
    console.log(previous_fiche)
    console.log(previous_fiche.length)
    if (previous_fiche.length) {
        const new_rank = previous_fiche.data("rang") - 1
        fiche.insertBefore(previous_fiche)
        $.ajax({
            url: "/change_rank/",
            type: "POST",
            data: {id: fiche_id, rank: new_rank, csrfmiddlewaretoken: csrf_token},
            success: function () {
                toastr.success('Nouveau rang sauvegardé avec succès')
            },
            error: function () {
                toastr.error('Erreur a la sauvegarde!')
            }
        })
    } else {
        toastr.warning("Ça se voit pas qu'il n'y a pas d'autre fiche ? :)")
    }
}