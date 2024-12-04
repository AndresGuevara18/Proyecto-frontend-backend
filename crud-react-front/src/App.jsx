import { useState, useEffect } from "react";//permiten gestionar el estado de los componentes funcionales

// Componente para renderizar cada usuario
function UsersItems({ id, tipoDocumento, numeroDoc, nombre, email, idCargo, handlerDeleteUserButton }) {
  return (
    <article className="w-96 bg-gray-100 rounded-xl shadow-lg shadow-gray-800 mx-auto my-10 mt-10 p-5">
      <p>ID: {id}</p>
      <p>Tipo documento: {tipoDocumento}</p>
      <p>Documento: {numeroDoc}</p>
      <p>Nombre: {nombre}</p>
      <p>Email: {email}</p>
      <p>Cargo: {idCargo}</p>
      <div className="flex justify-center my-5">
        <button className="bg-red-700 text-gray-100 w-32 font-semibold rounded-xl h-10 hover:bg-red-900 hover:text-gray-200 hover:cursor-pointer" onClick={handlerDeleteUserButton}>Eliminar</button>  
      </div>
      
    </article>
  );
}

function App() {
  const [users, setUsers] = useState([]); //oberter usuarios
  const [dataUserForm, setUserDataForm] = useState({}) //agregar usuario con objeto vaciio

  // Función asincrónica para obtener usuarios
  const getUsers = async () => {
    try {
      const allUsers = await fetch("http://localhost:8000/users/all"); // ruta del backend para obtener datos
      const usersJson = await allUsers.json(); // Convierte la respuesta a JSON
      console.log(usersJson); // Muestra los usuarios en la consola
      setUsers(usersJson); // Guarda los usuarios en el estado
    } catch (error) {
      console.log("Error al obtener usuarios:", error); // Muestra errores si los hay
    }
  };

  //funcion agregar usuario
  const handlerUserFormInput = (e) =>{
    setUserDataForm (//modificar el dataUserFromt
      {
        ...dataUserForm,//estruturar lo que esta dataUserForm
        [e.target.name]: e.target.value //modificar dato creando objeto se estrictura los elementos que no estan modificados
      }//se le pasa un objeto 
    )
  };

  //funcion quc ontrola cuando se envia en el formulario
  const handlesUserFormSubmit = async (e) =>{
    e.preventDefault() //
    //console.log(dataUserForm)
    await fetch("http://localhost:8000/users", {//ruta en user.py para agregar usuario
      method: "POST",
      //header igual a objeto
      headers: {
        "Content-Type" : "Application/json"
      },
      //body los datos que van al backend
      body: JSON.stringify(dataUserForm) //dar formato a los datos que estan en el form
    });

    getUsers();//llamdo a los usuario para que se  vea modificado en el front
  };

  //eliminar 
  const handlerDeleteUserButton = async (id) =>{//pasando el id a eliminar
    await fetch(`http://localhost:8000/users/${id}`, {//ruta en user.py para agregar usuario
      method: "DELETE"
    });

    getUsers()//actualizar estaod aplicacion
  };


  // Ejecutar la función al montar el componente
  useEffect(() => {
    getUsers();
  }, []); // Solo se ejecuta al cargar

  return (
    <main className="w-full min-h-screen bg-gray-300 text-gray-800">
      <h1 className="text-3xl font-bold text-center py-10">Cliente</h1>

      {/*Formulario*/}
      <form className="flex flex-col  justify-center items-center px-5" onSubmit={handlesUserFormSubmit}>
        <input  className="w-96 h-8 pl-3 text-gray-700 rounded-xl my-3" onChange={ handlerUserFormInput} value={dataUserForm.id } type="number" name="id" required placeholder="ID"></input>
        <input  className="w-96 h-8 pl-3 text-gray-700 rounded-xl my-3" onChange={ handlerUserFormInput} value={dataUserForm.tipoDocumento } type="text" name="tipoDocumento" required placeholder="Tipo documento"></input>
        <input  className="w-96 h-8 pl-3 text-gray-700 rounded-xl my-3" onChange={ handlerUserFormInput} value={dataUserForm.numeroDoc } type="text" name="numeroDoc" required placeholder="Numero documento"></input>
        <input  className="w-96 h-8 pl-3 text-gray-700 rounded-xl my-3" onChange={ handlerUserFormInput} value={dataUserForm.nombres } type="text" name="nombres" required placeholder="Nombre y apoellidos"></input>
        <input  className="w-96 h-8 pl-3 text-gray-700 rounded-xl my-3" onChange={ handlerUserFormInput} value={dataUserForm.email } type="text" name="email" required placeholder="Email"></input>
        <input  className="w-96 h-8 pl-3 text-gray-700 rounded-xl my-3" onChange={ handlerUserFormInput} value={dataUserForm.entidad } type="number" name="entidad" required placeholder="Entidad o cargo"></input>
        <input  className="h-10 w-32 bg-green-600 text-gray-100 rounded-xl font-semibold hover:cursor-pointer" type="submit" value="Crear"/>
      </form>

      <div>
        {/*como en la api get_all_users
        users.append({
                "id": row[0],
                "tipoDocumento": row[1],
                "numeroDoc": row[2],
                "nombres": row[3],
                "email": row[4],
                "entidad": row[5], 
            })*/}
        {users.length === 0
          ? "Cargando..."
          : users.map((us) => (
              <UsersItems
                key={us.id} // Clave correcta
                id={us.id}
                tipoDocumento={us.tipoDocumento}
                numeroDoc={us.numeroDoc} // Usar snake_case como en la API
                nombre={us.nombres} // Cambiar a "nombres" como en la API
                email={us.email}
                idCargo={us.entidad} // Cambiar a "entidad" como en la API
                handlerDeleteUserButton={() => handlerDeleteUserButton(us.id)} //como funcion anonima
                />
            ))}
      </div>
    </main>
  );
}

export default App;
