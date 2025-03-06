document.addEventListener('DOMContentLoaded', () => {
  const categoryGrid = document.getElementById('category-grid');
  if (categoryGrid) {
      categoryGrid.style.animation = 'loadGrid .3s linear forwards';
  } else {
      console.error("❌ Element #category-grid not found!");
  }
});
