function addStaff(pro_id, emp_id, csrf_token){
    // กำหนด path ให้ถูกต้อง

    fetch(`/project/project_detail/${pro_id}/${emp_id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
    })
    .then(data => {
        console.log('Item updated successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}


async function removeStaff(pro_id, emp_id, csrf_token){
    // กำหนด path ให้ถูกต้อง
    fetch(`/project/project_detail/${pro_id}/${emp_id}/`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
    })
    .then(data => {
        console.log('Item updated successfully')
        window.location.reload()
    })
    .catch(error => console.error('Error:', error));
}