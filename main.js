let currentPhoto = 0;
const photoContainer = document.getElementById('photoContainer');
const photos = document.querySelectorAll('.photo');

function scrollPhotos(direction) {
    if (direction === 'left') {
        currentPhoto = (currentPhoto - 1 + photos.length) % photos.length;
    } else {
        currentPhoto = (currentPhoto + 1) % photos.length;
    }

    updatePhotoDisplay();
}

function updatePhotoDisplay() {
    photoContainer.style.transform = `translateX(${-currentPhoto * 100}%)`;
}