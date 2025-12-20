BASE_URL = CONFIG.BASE_URL

// login

const login_form = document.querySelector('.login-form');
const login_box = document.querySelector('.login-box');
const auth_msg = document.querySelector('.auth-err-msg');




const login = async (data) => {
    try {
        const res = await fetch(`${BASE_URL}/auth/login/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
            credentials: 'include',
        })


        let returned_data = {};
        try {
            returned_data = await res.json();
        } catch (e) {}


        if(!res.ok) {
            auth_msg.style.color = 'red';
            auth_msg.style.visibility = 'visible';
            auth_msg.innerText = returned_data.detail || 'Log In failed. Try again...';
            return false;
        }

        return true;

    }
    catch(err) {
        console.log(err);
        auth_msg.style.color = 'red';
        auth_msg.style.visibility = 'visible';
        auth_msg.innerText = 'Server error. Try again later';
        return false;
    }
}

login_form.addEventListener('submit', async (e) => {
    e.preventDefault();
    auth_msg.style.visibility = 'hidden';

    const username = document.querySelector('#login-username').value.trim();
    const password = document.querySelector('#login-password').value;
    
    show_loader()

    const data = {
        'username': username, 
        'password': password,
    }
    
    const success = await login(data);

    if(success) {
        login_form.reset();
        window.location.href = 'index.html';
    }

    hide_loader('LOG IN');
})





// loader

const auth_submit_btn = document.querySelector('.auth-btn')

const show_loader = () => {
    auth_submit_btn.innerText = '';
    auth_submit_btn.disabled = true;
    auth_submit_btn.innerHTML = `<div class="loader"></div>`;
}

const hide_loader = (text) => {
    auth_submit_btn.innerText = text;
    auth_submit_btn.disabled = false;
}