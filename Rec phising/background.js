chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    if (changeInfo.status === 'complete' && tab.active && tab.url.startsWith('http')) {
        var url = tab.url;
        console.log('data before sending: ',JSON.stringify({ url: url }))
        // Send URL to server for processing
        fetch('http://localhost:8080/api/v1/Test', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: url }),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Handle server response here
            if(data.message !== 'ok'){
                console.log('web khong an toan')
            }else{
                console.log('web an toan');
                chrome.tabs.create({ url: chrome.runtime.getURL('popup2.html') });
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});
