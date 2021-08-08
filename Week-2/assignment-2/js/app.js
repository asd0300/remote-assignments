const listHeadText = document.querySelector(".name a");
const CallToActionButton = document.querySelector(".box");
const group2Boxs = document.getElementsByClassName('section_for_container')[1];

group2Boxs.style.visibility = 'hidden';
listHeadText.addEventListener("click", () => {
    listHeadText.textContent = "Have a Good Time!";                            
  });

CallToActionButton.addEventListener("click", () => {
    if(group2Boxs.style.visibility == 'hidden'){
        group2Boxs.style.visibility = 'visible';
    }

});