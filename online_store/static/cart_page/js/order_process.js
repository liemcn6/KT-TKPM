(function() {
  const form = document.getElementById('process-order-form');
  const checkboxes = Array.from(form?.querySelectorAll('input[type="checkbox"]'));
  const orderBtn = document.getElementById('order-btn');
  const orderMsgContainer = document.getElementById('order-msg');

  orderBtn.addEventListener('click', () => {
    const selectedItemIdList = checkboxes.reduce((total, checkbox) => {
      if(checkbox.checked) {
        total.push(checkbox.value);
      }

      return total;
    }, []);

    if(selectedItemIdList.length > 0) {
      window.localStorage.setItem('selectedItem', JSON.stringify(selectedItemIdList));
      window.location.pathname = '/order/process';
      return;
    }

    orderMsgContainer.innerText = 'Bạn chưa chọn sản phẩm để đặt hàng';
  });
})();