BASE_URL = CONFIG.BASE_URL

const user_name = document.querySelector('#hello-user')
const user_btn = document.querySelector('.user-box')
const body_loader = document.querySelector('.body-loader')
const logout_btn = document.querySelector('.logout')
const logout_text = document.querySelector('#logout-text')
const empty_image = document.querySelector('.empty-image')
const task_list = document.querySelector('.task-list')
const progress_num = document.querySelector('#progress-number')
const progress_bar = document.querySelector('.progress-fill')
const edit_btn = document.querySelector('.edit')
const task_title = document.querySelector('.task-title')
const status = document.querySelector('.status')
const add_task_btn = document.querySelector('.task-add-btn')
const add_task_input = document.querySelector('#task-add-input')
const delete_btn = document.querySelector('.delete')
const progressLoader = document.querySelector('.circle-loader');






task_list.addEventListener('click', (e) => {
    const deleteBtn = e.target.closest('.delete');
    if (!deleteBtn) return;

    const taskId = deleteBtn.dataset.id;

    const confirmDelete = confirm('Are you sure you want to delete this task?');
    if (!confirmDelete) return;

    deleteBtn.style.pointerEvents = 'none';

    delete_task(taskId);
});

const delete_task = async (task_id) => {
    showProgressLoader()
    console.log(`deleting ${task_id}`)
    try {
        const res = await fetch(`${BASE_URL}/tasks/delete/${task_id}`, {
            method: 'DELETE', 
            credentials: 'include',
        })

        let returned_data = null;
        const contentType = res.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            returned_data = await res.json();
        }
        
        // console.log(returned_data)
        
        if(!res.ok) {
            alert('Task deleting failed')
            return;
        }

        console.log('Deleting completed')
    }
    catch(err) {
        console.log(err);
    }
    finally {
        hideProgressLoader();
        fetch_all_task();
    }
}





document.addEventListener('DOMContentLoaded', () => {
    current_user();
    // fetch_all_task()
});

logout_btn.addEventListener('click', () => {
    logout();
})


add_task_btn.addEventListener('click', () => {
    let title = add_task_input.value.trim();
    const data = {
        'title': title, 
        'description': 'empty', 
        'status': 'pending'
    }
    if(title === '') {
        alert("Title can't be empty.");
        return;
    }
    console.log(title)
    create_task(data);
    add_task_input.value = '';
})



const create_task = async (data) => {
    showProgressLoader()
    try {
        const res = await fetch(`${BASE_URL}/tasks/create`, {
            method: 'POST', 
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })

        let returned_data = null;
        const contentType = res.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            returned_data = await res.json();
        }
        
        // console.log(returned_data)
        
        if(!res.ok) {
            alert('Task adding failed')
            return;
        }

        console.log('Adding completed')
    }
    catch(err) {
        console.log(err);
    }
    finally {
        hideProgressLoader()
        fetch_all_task();
    }
}


task_list.addEventListener('click', (e) => {
    const editBtn = e.target.closest('.edit');
    if (!editBtn) return;

    const taskBox = editBtn.closest('.task-box');
    const taskTitle = taskBox.querySelector('.task-title');
    const status = taskBox.querySelector('.status');
    const icon = editBtn.querySelector('i');
    const taskId = editBtn.dataset.id;

    // ENTER EDIT MODE
    if (!taskTitle.classList.contains('editing')) {
        taskTitle.classList.add('editing');
        status.classList.add('editing');
        status.disabled = false

        taskTitle.focus();
        icon.classList.replace('fa-pen-to-square', 'fa-check');
    }
    // EXIT / SAVE MODE
    else {
        taskTitle.classList.remove('editing');
        status.classList.remove('editing');

        icon.classList.replace('fa-check', 'fa-pen-to-square');

        // 🔥 here you will call API later
        console.log('Save:', {
            title: taskTitle.value,
            status: status.value
        });

        const data = {
            title: taskTitle.value,
            status: status.value
        }
        editBtn.disabled = true;
        update_task(data, taskId);
        editBtn.disabled = false;
    }
});


const update_task = async (data, task_id) => {
    console.log('updating the task...')
    showProgressLoader()
    console.log(task_id)
    try {
        const res = await fetch(`${BASE_URL}/tasks/update/${task_id}`, {
            method: 'PUT', 
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })

        let returned_data = null;
        const contentType = res.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            returned_data = await res.json();
        }
        
        // console.log(returned_data)
        
        if(!res.ok) {
            alert('updating failed...')
            return;
        }
        console.log('updating completed')
        // fetch_all_task();
    }
    catch(err) {
        console.log(err);
    }
    finally {
        hideProgressLoader();
        fetch_all_task();
    }
}





const fetch_all_task = async () => {
    console.log('fetching all task...');
    showProgressLoader();
    try {
        const res = await fetch(`${BASE_URL}/tasks`, {
            method: 'GET', 
            credentials: 'include',
        })

        let tasks = null;
        const contentType = res.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            tasks = await res.json();
        }

        if(!res.ok) {
            console.log('tasks fetching failed')
            return;
        }

        if(tasks.length !== 0) {
            task_list.innerHTML = '';
            empty_image.style.display = 'none';
            complete_task = 0;
            tasks.forEach(element => {
                let task_box = document.createElement('div')
                task_box.classList.add('task-box')
                let checked = '';
                if(element.status == 'completed') {
                    checked = 'checked';
                    complete_task = complete_task+1;
                }
                task_box.innerHTML = `
                    <select name="status" class="status" disabled>
                        <option value="pending" ${element.status === 'pending' ? 'selected' : ''}>
                            Pending
                        </option>
                        <option value="in_progress" ${element.status === 'in_progress' ? 'selected' : ''}>
                            In Progress
                        </option>
                        <option value="completed" ${element.status === 'completed' ? 'selected' : ''}>
                            Completed
                        </option>
                    </select>
                    <input type="text" class="task-title" value="${element.title}"></input>
                    <div class="edit" data-id="${element.id}">
                        <i class="fa-solid fa-pen-to-square"></i>
                    </div>
                    <div class="delete" data-id="${element.id}">
                        <i class="fa-solid fa-trash"></i>
                    </div>
                `
                task_list.append(task_box)
            });

            progress_num.innerText = tasks.length? `${complete_task}/${tasks.length}`: `0/0`;
            let percent = (complete_task / tasks.length) * 100
            progress_bar.style.width = `${percent}%`
        }
        else {
            task_list.innerHTML = '';
            empty_image.style.display = 'block';
            progress_num.innerText = '0/0';
        }

        console.log('Fetching completed')
    }
    catch(err) {
        console.log(err);
    }
    finally {
        hideProgressLoader();
    }

}


const current_user = async () => {
    showProgressLoader();
    console.log('fetching current user...')
    user_name.innerText = `Fetching user...`;
    logout_btn.disabled = true;
    logout_btn.style.cursor = 'default';
    // show_body_loader()
    try {
        const res = await fetch(`${BASE_URL}/auth/me`, {
            method: 'GET', 
            credentials: 'include',
        })

        let returned_data = null;
        const contentType = res.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            returned_data = await res.json();
        }
        
        // console.log(returned_data)
        
        if(!res.ok) {
            console.log('auth failed, redirecting...')
            window.location.href = 'login.html'; // or login.html
            return;
        }

        user_name.innerText = `Hello, ${returned_data.name}...`;
        console.log('User fetched')
    }
    catch(err) {
        console.log(err);
        window.location.href = 'login.html';
        hideProgressLoader()
    }
    finally {
        // hide_body_loader()
        logout_btn.disabled = false;
        logout_btn.style.cursor = 'pointer';
        hideProgressLoader();
        fetch_all_task();
    } 
}


const logout = async () => {
    showProgressLoader()
    logout_text.innerText = 'Loading...'
    logout_btn.disabled = true
    try {
        let res = await fetch(`${BASE_URL}/auth/logout`, {
            method: 'POST', 
            credentials: 'include'
        })
        
        let returned_data = null;
        const contentType = res.headers.get('content-type');
        if (contentType && contentType.includes('application/json')) {
            returned_data = await res.json();
        }
        window.location.href = 'login.html';
        return;

    }
    catch(err) {
        console.log(err)
        alert('Logout failed')
    }
    finally {
        logout_text.innerText = 'Log Out';
        logout_btn.disabled = false;
        hideProgressLoader()
    }
}








const showProgressLoader = () => {
    progressLoader.classList.remove('hidden');
    progress_num.classList.add('hidden');
};

const hideProgressLoader = () => {
    progressLoader.classList.add('hidden');
    progress_num.classList.remove('hidden');
};







// const show_body_loader = () => {
//     body_loader.style.display = 'flex';
// }
// const hide_body_loader = () => {
//     body_loader.style.display = 'none';
// }

// const logout_loader_btn = (node) => {
//     node.innerText = '...';
//     node.disabled = true;
// }

// const hide_loader_btn = (node, text) => {
//     node.innerText = text;
//     node.disabled = false;
// }
