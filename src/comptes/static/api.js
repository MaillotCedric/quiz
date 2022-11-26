let nouvel_utilisateur = {
    "username": "toto",
    "password": "azerty",
    "matricule": "CCCC",
    "codeSecteur": "RD",
    "codeRole": "collab"
};

let matricule = "CCCC";

let url_delete_user = "../api/delete?matricule=" + matricule;

let my_chart = null;

function afficher_graph(json) {
    const ctx = document.getElementById('myChart');

    let x = json.map((element) => {
        return element.codeSecteur;
    });
    let y = json.map((element) => {
        return element.dcount;
    });

    if (my_chart !== null) {
        my_chart.destroy();
    }

    my_chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: x,
            datasets: [{
                label: 'employés/secteurs',
                data: y,
                borderWidth: 1,
                backgroundColor: '#9BD0F5'
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
};

function update_graph(json) {
    $.get("../api/secteurs?format=json", function(data, status) {
        afficher(data);
        afficher_graph(data);
    });
};

function afficher(json) {
    console.log("afficher");
    console.log(json);
};

function rest(url, data, f=afficher) {
    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    $.ajax({
        type:'POST',
        url: url,
        headers:{'X-CSRFToken': csrftoken},
        data: data,
        success: function(json) {
            f(json)
        },
        error: function(erreur) {}
    })
};

function ajax_call(methode, ajax_url, donnees, success_callback, error_callback) {
    let csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    $.ajax({
        type: methode,
        url: ajax_url,
        headers:{'X-CSRFToken': csrftoken},
        data: donnees,
        success: function(json) {
            success_callback(json)
        },
        error: function(erreur) {
            error_callback(erreur)
        }
    })
}

function ajouter_ajax_call(element_id, methode, ajax_url, donnees={}, success_callback=afficher, error_callback=afficher) {
    $(document).on('submit', element_id, function(event){
        event.preventDefault();
    
        ajax_call(methode, ajax_url, donnees, success_callback, error_callback); 
    });
}

ajouter_ajax_call("#ajax-call", "POST", "../api/add", nouvel_utilisateur, update_graph)

ajouter_ajax_call("#ajax-delete", "POST", url_delete_user, {}, update_graph)

ajouter_ajax_call("#ajax-graph", "GET", "../api/secteurs?format=json", {}, afficher_graph)
