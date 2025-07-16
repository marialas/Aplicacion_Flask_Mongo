// static/js/app.js

async function loginUsuario(e) {
  e.preventDefault();
  const form = document.getElementById("formLogin");
  const datos = {
    usuario: form.usuario.value,
    password: form.password.value
  };
  const res = await fetch("/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos)
  });
  const data = await res.json();
  if (data.estado) {
    location.href = "/";
  } else {
    document.getElementById("mensajeLogin").innerText = data.mensaje;
  }
}

// Listar géneros al cargar la vista
async function cargarGeneros() {
  const res = await fetch("/genero/");
  const data = await res.json();
  const tabla = document.getElementById("tablaGeneros");
  tabla.innerHTML = "";

  data.generos.forEach(g => {
    tabla.innerHTML += `
      <tr>
        <td>${g.nombre}</td>
        <td>
          <button onclick="mostrarEditarGenero('${g._id}', '${g.nombre}')">Editar</button>
          <button onclick="eliminarGenero('${g._id}')">Eliminar</button>
        </td>
      </tr>
    `;
  });

  if ($.fn.DataTable.isDataTable('#tablaGeneros')) {
    $('#tablaGeneros').DataTable().destroy();
  }
  $('#tablaGeneros').DataTable();
}


// Agregar género
async function agregarGenero(e) {
  e.preventDefault();
  const nombre = document.getElementById("nombre").value;

  const res = await fetch("/genero/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre })
  });

  const data = await res.json();
  const mensaje = document.getElementById("mensajeGenero");

  if (data.estado) {
    mensaje.textContent = "✅ Género agregado correctamente.";
    document.getElementById("formGenero").reset();
  } else {
    mensaje.textContent = "❌ Error: " + data.mensaje;
  }
}

// Eliminar género
async function eliminarGenero(id) {
  if (!confirm("¿Estás seguro de eliminar este género?")) return;

  const res = await fetch(`/genero/${id}`, {
    method: "DELETE"
  });

  const data = await res.json();
  alert(data.mensaje);
  cargarGeneros();
}

// Mostrar prompt para editar género
function mostrarEditarGenero(id, nombreActual) {
  const nuevoNombre = prompt("Editar nombre del género:", nombreActual);
  if (nuevoNombre && nuevoNombre !== nombreActual) {
    editarGenero(id, nuevoNombre);
  }
}

// Editar género
async function editarGenero(id, nombre) {
  const res = await fetch(`/genero/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre })
  });

  const data = await res.json();
  alert(data.mensaje);
  cargarGeneros();
}


async function cargarPeliculas() {
  const res = await fetch("/pelicula/");
  const data = await res.json();
  const tabla = document.getElementById("tablaPeliculas");
  tabla.innerHTML = "";

  data.peliculas.forEach(p => {
    tabla.innerHTML += `
      <tr>
        <td>${p.codigo}</td>
        <td>${p.titulo}</td>
        <td>${p.protagonista}</td>
        <td>${p.duracion}</td>
        <td>${p.resumen}</td>
        <td>${p.genero}</td>
        <td><img src="${p.foto}" width="60"></td>
        <td>
          <a href="/vistaEditarPelicula/${p.id}">✏️</a>
          <button onclick="eliminarPelicula('${p.id}')">🗑️</button>
        </td>
      </tr>
    `;
  });

  //  Inicializar DataTables DESPUÉS de cargar las filas
  if ($.fn.DataTable.isDataTable('#tablaPeliculas')) {
    $('#tablaPeliculas').DataTable().destroy(); 
  }
  $('#tablaPeliculas').DataTable(); 
}


async function agregarPelicula(e) {
  e.preventDefault();
  const form = e.target;
  const datos = {
    codigo: parseInt(form.codigo.value),
    titulo: form.titulo.value,
    protagonista: form.protagonista.value,
    duracion: parseInt(form.duracion.value),
    resumen: form.resumen.value,
    foto: form.foto.value,
    genero: form.genero.value
  };

  const res = await fetch("/pelicula/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos)
  });

  const data = await res.json();
  const mensaje = document.getElementById("mensajePelicula");
  if (res.ok) {
    mensaje.textContent = "✅ Película agregada.";
    form.reset();
  } else {
    mensaje.textContent = "❌ " + data.mensaje;
  }
}

async function eliminarPelicula(id) {
  if (!confirm("¿Seguro que quieres eliminar esta película?")) return;

  const res = await fetch(`/pelicula/${id}`, { method: "DELETE" });
  const data = await res.json();
  alert(data.mensaje);
  cargarPeliculas();
}

async function editarPelicula(e) {
  e.preventDefault();
  const form = e.target;
  const id = form.id.value;
  const datos = {
    codigo: parseInt(form.codigo.value),
    titulo: form.titulo.value,
    protagonista: form.protagonista.value,
    duracion: parseInt(form.duracion.value),
    resumen: form.resumen.value,
    foto: form.foto.value,
    genero: form.genero.value
  };

  const res = await fetch(`/pelicula/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(datos)
  });

  const data = await res.json();
  const mensaje = document.getElementById("mensajeEditar");
  if (res.ok) {
    mensaje.textContent = "✅ Película actualizada";
  } else {
    mensaje.textContent = "❌ " + data.mensaje;
  }
}

