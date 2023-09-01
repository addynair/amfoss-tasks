const apiKey = "a14e6b46a8b33f9969cff534ff9cd6a7"

document.getElementById("searchButton").addEventListener("click", getWeatherDetails);




async function getState(city){
     let response = await fetch(`http://api.openweathermap.org/geo/1.0/direct?q=${city}&appid=${apiKey}`)
     let data = await response.json()
     return data
}

async function getUsers(lat, lon){
    let response = await fetch(`https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&appid=${apiKey}`)
    let data = await response.json()
    return data
}



function getWeatherDetails(){
    const cityname = document.getElementById('cityInput').value

    getState(cityname).then(data => {
        getUsers(parseFloat(data[0].lat).toFixed(2),
            parseFloat(data[0].lon).toFixed(2)).then(
                weatherData => {
                    console.log(weatherData)
                    const tempElement = document.getElementById('temp')
                    const cityElement = document.getElementById('cityName')
                    const descElement = document.getElementById('description')

                    cityElement.innerHTML = cityname
                    descElement.innerHTML = weatherData.weather[0].description
                    tempElement.innerHTML = weatherData.main.temp
                }
    
                
            )
    })
}

 

