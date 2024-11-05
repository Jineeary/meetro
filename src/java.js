// 지도를 표시할 div 
var mapContainer = document.getElementById('map'); 

// 지도 옵션
var mapOption = { 
    center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
    level: 3 // 지도의 확대 레벨
};

// 지도 생성
var map = new kakao.maps.Map(mapContainer, mapOption); 
