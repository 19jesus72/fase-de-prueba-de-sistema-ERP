from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_mensajes_flash'

# Datos de ejemplo para simular una base de datos
usuarios_ejemplo = {
    1: {
        'id': 1,
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'fecha_nacimiento': '1990-05-15',
        'correo': 'juan.perez@mastercontrol.com.ec',
        'telefono': '+1234567890',
        'direccion': 'Calle Principal 123, Ciudad',
        'cargo': 'administrador'
    },
    2: {
        'id': 2,
        'nombre': 'María',
        'apellido': 'González',
        'fecha_nacimiento': '1985-11-22',
        'correo': 'maria.gonzalez@mastercontrol.com.ec',
        'telefono': '+0987654321',
        'direccion': 'Avenida Central 456, Ciudad',
        'cargo': 'supervisor'
    }
}

@app.route('/')
def inicio_usuarios():
    return render_template('usuarios.html')

@app.route('/crear_usuario', methods=['GET', 'POST'])
def crear_usuario():
    """
    Ruta para la creación de nuevos usuarios.
    GET: Muestra el formulario de creación
    POST: Procesa los datos del formulario
    """
    if request.method == 'POST':
        # Aquí procesaríamos los datos del formulario
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        # ... procesar otros campos

        # Mostrar mensaje de éxito (en una implementación real, guardaríamos en BD)
        flash('Usuario creado exitosamente', 'success')
        return redirect(url_for('inicio_usuarios'))

    return render_template('crear_usuario.html')


@app.route('/editar_usuario/<int:usuario_id>', methods=['GET', 'POST'])
def editar_usuario(usuario_id):
    """
    Ruta para la edición de usuarios existentes.
    GET: Muestra el formulario de edición con los datos actuales
    POST: Procesa los datos actualizados del formulario
    """
    usuario = usuarios_ejemplo.get(usuario_id)

    if not usuario:
        flash('Usuario no encontrado', 'error')
        return redirect(url_for('inicio_usuarios'))

    if request.method == 'POST':
        # Aquí procesaríamos los datos actualizados del formulario
        usuario['nombre'] = request.form.get('nombre')
        usuario['apellido'] = request.form.get('apellido')
        usuario['fecha_nacimiento'] = request.form.get('fecha_nacimiento')
        usuario['correo'] = request.form.get('correo')
        usuario['telefono'] = request.form.get('telefono')
        usuario['direccion'] = request.form.get('direccion')
        usuario['cargo'] = request.form.get('cargo')

        # Mostrar mensaje de éxito
        flash('Usuario actualizado exitosamente', 'success')
        return redirect(url_for('inicio_usuarios'))

    return render_template('editar_usuario.html', usuario=usuario)


@app.route('/lista_usuarios')
def lista_usuarios():
    return render_template('lista_usuarios.html', usuarios=usuarios_ejemplo)


@app.route('/eliminar_usuario/<int:usuario_id>', methods=['POST'])
def eliminar_usuario(usuario_id):
    if usuario_id in usuarios_ejemplo:
        # En una aplicación real, aquí eliminaríamos el usuario de la base de datos
        del usuarios_ejemplo[usuario_id]
        flash('Usuario eliminado exitosamente', 'success')
    else:
        flash('Usuario no encontrado', 'error')

    return redirect(url_for('lista_usuarios'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)