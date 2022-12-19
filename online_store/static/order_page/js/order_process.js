(function() {
  const selectedItemList = (window.localStorage.getItem('selectedItem'));
  const submitBtn = document.getElementById('sumbit-btn');
  const selectedItemInput = document.getElementById('selected-item');
  const processOrderForm = document.getElementById('process-order-form');

  submitBtn.addEventListener('click', () => {
    selectedItemInput.value = selectedItemList;
    processOrderForm.submit();
  });
})();