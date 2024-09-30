document.addEventListener('DOMContentLoaded', function() {
  const excerpts = document.querySelectorAll('.raw-excerpt');
  
  excerpts.forEach(excerpt => {
    const rawHtml = excerpt.innerHTML;
    const cleanText = rawHtml.replace(/<\/?[^>]+(>|$)/g, "");
    excerpt.textContent = cleanText;
  });
});
