import folium
import os

# Coordenadas dos pontos (exemplo)
locations = {
    'Futuro-Haus': (48.148605, 11.569874),
    'University Library of the Technische Universität München': (48.149832, 11.568195),
    'Gabelsbergerstraße 35': (48.148503, 11.567251),
    'Luisenstraße 18': (48.148120, 11.565986),
    'Brienner Str. 34': (48.146326, 11.567641),
    'Karolinenpl. 1': (48.142982, 11.566794),
    'Glasbrunnen, Brienner Str. 18': (48.145105, 11.569073),
    'Siemens AG - Corporate Headquarters Werner-von-Siemens-Straße 1': (48.144972, 11.567615),
    'Finanzgarten 80539 Munich': (48.140194, 11.580824),
    'Luitpoldblock Brienner Str. 11': (48.144176, 11.568932),
    'AWS - Amazon Web Services, Oskar-von-Miller-Ring 20': (48.146845, 11.573912),
}


# Criar o mapa centrado no ponto de início
m = folium.Map(location=locations['Futuro-Haus'], zoom_start=15)

# Adicionar os marcadores
for name, coord in locations.items():
    folium.Marker(coord, popup=name).add_to(m)

# Adicionar rotas (exemplo para 3 grupos)
routes = {
    'Grupo 1': ['Futuro-Haus', 'University Library of the Technische Universität München', 'Gabelsbergerstraße 35', 'Luisenstraße 18', 'Brienner Str. 34', 'Karolinenpl. 1', 'Glasbrunnen, Brienner Str. 18', 'Futuro-Haus'],
    'Grupo 2': ['Futuro-Haus', 'Gabelsbergerstraße 35', 'University Library of the Technische Universität München', 'Luisenstraße 18', 'Karolinenpl. 1', 'Brienner Str. 34', 'Glasbrunnen, Brienner Str. 18', 'Futuro-Haus'],
    'Grupo 3': ['Futuro-Haus', 'Luisenstraße 18', 'Gabelsbergerstraße 35', 'University Library of the Technische Universität München', 'Karolinenpl. 1', 'Brienner Str. 34', 'Glasbrunnen, Brienner Str. 18', 'Futuro-Haus'],
    'Grupo 4': ['Futuro-Haus', 'Brienner Str. 34', 'Luisenstraße 18', 'Gabelsbergerstraße 35', 'University Library of the Technische Universität München', 'Karolinenpl. 1', 'Glasbrunnen, Brienner Str. 18', 'Futuro-Haus'],
    'Grupo 5': ['Futuro-Haus', 'Karolinenpl. 1', 'Brienner Str. 34', 'Luisenstraße 18', 'Gabelsbergerstraße 35', 'University Library of the Technische Universität München', 'Glasbrunnen, Brienner Str. 18', 'Futuro-Haus'],
    'Grupo 6': ['Futuro-Haus', 'Glasbrunnen, Brienner Str. 18', 'Karolinenpl. 1', 'Brienner Str. 34', 'Luisenstraße 18', 'Gabelsbergerstraße 35', 'University Library of the Technische Universität München', 'Futuro-Haus'],
    'Grupo 7': ['Futuro-Haus', 'Siemens AG - Corporate Headquarters Werner-von-Siemens-Straße 1', 'Finanzgarten 80539 Munich', 'Luitpoldblock Brienner Str. 11', 'AWS - Amazon Web Services, Oskar-von-Miller-Ring 20', 'Futuro-Haus'],
    'Grupo 8': ['Futuro-Haus', 'Luitpoldblock Brienner Str. 11', 'Siemens AG - Corporate Headquarters Werner-von-Siemens-Straße 1', 'Finanzgarten 80539 Munich', 'AWS - Amazon Web Services, Oskar-von-Miller-Ring 20', 'Futuro-Haus'],
    'Grupo 9': ['Futuro-Haus', 'AWS - Amazon Web Services, Oskar-von-Miller-Ring 20', 'Luitpoldblock Brienner Str. 11', 'Siemens AG - Corporate Headquarters Werner-von-Siemens-Straße 1', 'Finanzgarten 80539 Munich', 'Futuro-Haus'],
    'Grupo 10': ['Futuro-Haus', 'Finanzgarten 80539 Munich', 'AWS - Amazon Web Services, Oskar-von-Miller-Ring 20', 'Luitpoldblock Brienner Str. 11', 'Siemens AG - Corporate Headquarters Werner-von-Siemens-Straße 1', 'Futuro-Haus'],
}


colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightblue', 'darkgreen', 'darkpurple', 'darkorange']


for i, (group, route) in enumerate(routes.items()):
    color = colors[i]
    folium.PolyLine([locations[point] for point in route], color=color, weight=2.5, opacity=1).add_to(m)


# Salvar o mapa como HTML
m.save('mapa_fotografia.html')

# Abrir no navegador
os.system('start mapa_fotografia.html')
