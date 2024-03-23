let alarms = [];

function updateTime() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');
    document.getElementById('time').innerText = `${hours}:${minutes}:${seconds}`;

    checkAlarms(hours, minutes);
}

function setAlarm() {
    const alarmTime = document.getElementById('alarmTime').value;
    alarms.push(alarmTime);
    displayAlarms();
}

function displayAlarms() {
    const alarmsList = document.getElementById('alarmsList');
    alarmsList.innerHTML = '';
    alarms.forEach(alarm => {
        const alarmItem = document.createElement('div');
        alarmItem.innerText = `Alarm set for ${alarm}`;
        alarmsList.appendChild(alarmItem);
    });
}

function checkAlarms(hours, minutes) {
    const currentTime = `${hours}:${minutes}`;
    alarms.forEach(alarm => {
        if (alarm === currentTime) {
            alert('Alarm!');
        }
    });
}

setInterval(updateTime, 1000);
