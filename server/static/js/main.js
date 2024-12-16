document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM Content Loaded');
    const sidebar = document.getElementById('sidebar');
    const toggleBtn = document.getElementById('toggle-btn');
    const body = document.body;

    console.log('Sidebar:', sidebar);
    console.log('Toggle button:', toggleBtn);

    if (!sidebar || !toggleBtn) {
        console.error('No se encontraron los elementos necesarios');
        return;
    }

    toggleBtn.addEventListener("click", function () {
        console.log('Toggle button clicked');
        sidebar.classList.toggle("expand");
        body.classList.toggle("sidebar-expanded");
        console.log('Sidebar classes:', sidebar.classList);
    });

    function handleResponsive() {
        console.log('Window resized:', window.innerWidth);
        if (window.innerWidth <= 768) {
            sidebar.classList.remove("expand");
            body.classList.remove("sidebar-expanded");
        }
    }

    window.addEventListener('resize', handleResponsive);
    handleResponsive();
});