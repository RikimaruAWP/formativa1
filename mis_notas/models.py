# Create your models here.

class Notes:
    def __init__(self, title, description, is_important):
        self.title = title
        self.description = description
        self.is_important = is_important

class Listado:
    def __init__(self) -> None:
        self.list = []
        
    def buscar_notas(self, title):  # Cambiado a minúsculas
        for b in self.list:
            if title == b.title:
                return b 
        return None
 
    def eliminar(self, title):  # Cambiado a minúsculas
        result = self.buscar_notas(title)  # Actualizado para usar el nuevo nombre
        if result is not None and isinstance(result, Notes):
            self.list.remove(result)
            return 'La nota se eliminó correctamente'
        else:
            return 'La nota no se encuentra'
        
    def agregar(self, notes):
        if not isinstance(notes, Notes):
            return 'Debe agregar una nota válida'
        result = self.buscar_notas(notes.title)  # Actualizado para usar el nuevo nombre
        if result is not None:
            return 'Esta nota ya existe'
        self.list.append(notes)
        return 'Nota agregada'
