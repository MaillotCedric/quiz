let button = document.getElementById("btn-import-csv");
let fileInput = document.getElementById("fileInput");

function est_visible(btn) {
    return !btn.classList.value.split(" ").includes("d-none");
};

function enlever_classe(nom_classe, element_html) {
    element_html.classList.remove(nom_classe);
};

if (fileInput !== null) {
    fileInput.addEventListener("input", () => {
        if (!est_visible(button)) {
            enlever_classe("d-none", button);
        }
    });
}
