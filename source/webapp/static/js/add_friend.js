function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

async function makeRequest(url, method = 'GET', data = undefined) {
    let opts = {method, headers: {}};

    if (!csrfSafeMethod(method))
        opts.headers['X-CSRFToken'] = getCookie('csrftoken');

    if (data) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(data);
    }

    let response = await fetch(url, opts);

    if (response.ok) {  // нормальный ответ
        return response;
    } else {            // ошибка
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function addFriend(event) {
    event.preventDefault();
    let friend = event.target;
    console.log(friend)
    let id = friend.id;
    console.log(id)
    let url = friend.href;
    console.log(url)
    let remove = friend.parentElement.childNodes[2]
    console.log(remove)
    try {
        let response = await makeRequest(url, 'POST', {'id': id}).then((response) => response.json());
        if (response['add'] === 'add'){
             friend.style.display = 'none';
             remove.style.display = 'inline';
        }
        console.log(response)
    } catch (error) {
        console.log(error);
    }
}


async function deleteFriend(event) {
    event.preventDefault();
    let friend = event.target;
    console.log(friend)
    let id = friend.id;
    console.log(id)
    let url = friend.href;
    console.log(url)
    friend.style.display = 'none'
    let add = friend.parentElement.childNodes[0]
    console.log(add)

    try {
        let response = await makeRequest(url, 'DELETE', {'id': id}).then((response) => response.json());

        if (response['remove'] === 'remove'){
            add.style.display = 'inline';
        }
        console.log(response)
    } catch (error) {
        console.log(error);
    }
}
