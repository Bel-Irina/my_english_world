document.addEventListener('DOMContentLoaded', function() {
    // Flip flashcard on click
    const flashcards = document.querySelectorAll('.flashcard');
    flashcards.forEach(card => {
        card.addEventListener('click', function(e) {
            // Don't flip if delete button was clicked
            if (e.target.closest('.btn-delete') || e.target.closest('.delete-form')) {
                return;
            }
            this.classList.toggle('flipped');
        });
    });

    // Confirm before deletion
    const deleteForms = document.querySelectorAll('.delete-form');
    deleteForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!confirm('Вы уверены, что хотите удалить?')) {
                e.preventDefault();
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Toggle sidebar on mobile
    const sidebarToggle = document.createElement('button');
    sidebarToggle.className = 'btn btn-secondary d-md-none fixed-top m-3';
    sidebarToggle.innerHTML = '<i class="fas fa-bars"></i>';
    sidebarToggle.onclick = function() {
        document.querySelector('.sidebar').classList.toggle('show');
    };
    document.body.prepend(sidebarToggle);
    
    // Add media query listener
    function handleMobileView() {
        const sidebar = document.querySelector('.sidebar');
        if (window.innerWidth <= 768) {
            sidebar.classList.remove('show');
        } else {
            sidebar.classList.add('show');
        }
    }
    
    window.addEventListener('resize', handleMobileView);
    handleMobileView();
});