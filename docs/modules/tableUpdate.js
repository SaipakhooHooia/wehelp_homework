export function tableUpdate() {
//--------------處理周間白天天氣資訊--------------
    for(let i = 0; i < 7; i++){
        let container = document.createElement("div");
        container.style.backgroundColor = "#fff";
        container.style.flexDirection = "column";
        let signal = document.createElement("span");
        signal.className = "signal";
        let weatherImage = document.createElement("img");
        let temperature = document.createElement("span");
        temperature.className = "weekly-temperature";
        temperature.textContent = "25";
        signal.appendChild(weatherImage);
        container.appendChild(signal);
        container.appendChild(temperature);
        document.querySelector(".column-day").appendChild(container);
    };

    //--------------處理周間晚上天氣資訊--------------
    for(let i = 0; i < 7; i++){
        let container = document.createElement("div");
        container.style.backgroundColor = "#fff";
        container.style.flexDirection = "column";
        let signal = document.createElement("span");
        signal.className = "signal";
        let weatherImage = document.createElement("img");
        let temperature = document.createElement("span");
        temperature.className = "weekly-temperature";
        temperature.textContent = "25";
        signal.appendChild(weatherImage);
        container.appendChild(signal);
        container.appendChild(temperature);
        document.querySelector(".column-night").appendChild(container);
    };

    //--------------處理周間體感溫度資訊--------------
    for(let i = 0; i < 7; i++){
        let container = document.createElement("div");
        container.style.backgroundColor = "#fff";
        container.style.flexDirection = "column";
        let temperature = document.createElement("span");
        temperature.className = "weekly-temperature";
        temperature.textContent = "25";
        container.appendChild(temperature);
        document.querySelector(".column-real-feel").appendChild(container);
    };

    //--------------處理周間紫外線資訊--------------
    for(let i = 0; i < 7; i++){
        let container = document.createElement("div");
        container.style.backgroundColor = "#fff";
        container.classList.add("UV-ray-container", "purple");
        container.style.flexDirection = "column";
        let temperature = document.createElement("span");
        temperature.className = "weekly-temperature";
        temperature.textContent = "25";
        temperature.style.fontWeight = "bold";
        container.appendChild(temperature);
        document.querySelector(".column-UV-ray").appendChild(container);
    };
};