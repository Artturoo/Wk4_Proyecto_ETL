#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Para la primera tabla dfprecio. Sacamos id por provincias. Luego haremos lo mismo con la segunda tabla...
column=[]
for e in dfprecio['Capital']:
    if 'San Sebastián' in e:
        e =e.replace('San Sebastián', '13')
        column.append(e)        
    elif 'Madrid' in e:
        e =e.replace('Madrid', '11')
        column.append(e)    
    elif 'Bilbao' in e:
        e =e.replace('Bilbao', '13')
        column.append(e) 
    
    elif 'Vitoria' in e:
        e =e.replace('Vitoria', '13')
        column.append(e)
    elif 'Cádiz' in e:
        e =e.replace('Cádiz', '1')
        column.append(e)
    elif 'Pamplona' in e:
        e =e.replace('Pamplona', '12')
        column.append(e)
    elif 'Málaga' in e:
        e =e.replace('Málaga', '1')
        column.append(e)
    elif 'BILBAO' in e:
        e =e.replace('BILBAO', '13')
        column.append(e)
    elif 'Sevilla' in e:
        e =e.replace('Sevilla', '1')
        column.append(e)
        
    
    elif 'Gerona/Girona' in e:
        e =e.replace('Gerona/Girona', '7')
        column.append(e)       
    elif 'Coruña (La)' in e:
        e =e.replace('Coruña (La)', '10')
        column.append(e)
    elif 'Santander' in e:
        e =e.replace('Santander', '4')
        column.append(e)
    elif 'Valencia/València' in e:
        e =e.replace('Valencia/València', '8')
        column.append(e)
    elif 'Granada' in e:
        e =e.replace('Granada', '1')
        column.append(e)
    elif 'Salamanca' in e:
        e =e.replace('Salamanca', '5')
        column.append(e)
    elif 'Zaragoza' in e:
        e =e.replace('Zaragoza', '2')
        column.append(e)
    elif 'Alicante/Alacant' in e:
        e =e.replace('Alicante/Alacant', '8')
        column.append(e)
    elif 'Tarragona' in e:
        e =e.replace('Tarragona', '7')
        column.append(e)
    elif 'Córdoba' in e:
        e =e.replace('Córdoba', '1')
        column.append(e)
    elif 'Valladolid' in e:
        e =e.replace('Valladolid', '5')
        column.append(e)
    elif 'Burgos' in e:
        e =e.replace('Burgos', '5')
        column.append(e)
    elif 'Guadalajara' in e:
        e =e.replace('Guadalajara', '6')
        column.append(e)
    elif 'Oviedo' in e:
        e =e.replace('Oviedo', '3')
        column.append(e)
    elif 'Segovia' in e:
        e =e.replace('Segovia', '11')
        column.append(e)
    elif 'Toledo' in e:
        e =e.replace('Toledo', '6')
        column.append(e)
    elif 'Huesca' in e:
        e =e.replace('Huesca', '2')
        column.append(e)
    elif 'Almería' in e:
        e =e.replace('Almería', '1')
        column.append(e)
    elif 'Logroño' in e:
        e =e.replace('Logroño', '14')
        column.append(e)
    elif 'Teruel' in e:
        e =e.replace('Teruel', '2')
        column.append(e)
    elif 'Murcia' in e:
        e =e.replace('Murcia', '0')
        column.append(e)
    elif 'Palencia' in e:
        e =e.replace('Palencia', '5')
        column.append(e)
    elif 'Badajoz' in e:
        e =e.replace('Badajoz', '9')
        column.append(e)
    elif 'Pontevedra' in e:
        e =e.replace('Pontevedra', '10')
        column.append(e)
    elif 'Orense/Ourens' in e:
        e =e.replace('Orense/Ourens', '10')
        column.append(e)
    elif 'Albacete' in e:
        e =e.replace('Albacete', '6')
        column.append(e)
    elif 'Huelva' in e:
        e =e.replace('Huelva', '1')
        column.append(e)
    elif 'Jaén' in e:
        e =e.replace('Jaén', '1')
        column.append(e)
    elif 'Cuenca' in e:
        e =e.replace('Cuenca', '6')
        column.append(e)
    elif 'Cáceres' in e:
        e =e.replace('Cáceres', '9')
        column.append(e)
    elif 'Castellón/Castellón' in e:
        e =e.replace('Castellón/Castellón', '8')
        column.append(e)
    elif 'Lérida/Lleida' in e:
        e =e.replace('Lérida/Lleida', '7')
        column.append(e)
    elif 'Ávila' in e:
        e =e.replace('Ávila', '5')
        column.append(e)
    elif 'Lugo' in e:
        e =e.replace('Lugo', '10')
        column.append(e)
    elif 'Soria' in e:
        e =e.replace('Soria', '5')
        column.append(e)
    elif 'Ciudad Real' in e:
        e =e.replace('Ciudad Real', '6')
        column.append(e)  
    elif 'Zamora' in e:
        e =e.replace('Zamora', '5')
        column.append(e)
    
    else:
        e=e.replace(e,'0')
        column.append(e)
  




  # para la segunda tabla 

column2=[]
for e in tablapro['Provincia']:
    if 'Albacete' in e:
        e =e.replace('Albacete', '6')
        column.append(e)        
    elif 'Alicante/Alacan' in e:
        e =e.replace('Alicante/Alacan', '8')
        column.append(e)    
    elif 'Almería' in e:
        e =e.replace('Almería', '1')
        column.append(e) 
    
    elif 'Logroño' in e:
        e =e.replace('Logroño', '14')
        column.append(e)
    elif 'ZARAGOZA' in e:
        e =e.replace('ZARAGOZA', '2')
        column.append(e)
    elif 'ALACANT/ALICANTE' in e:
        e =e.replace('ALACANT/ALICANTE', '8')
        column.append(e)
    elif 'REUS' in e:
        e =e.replace('REUS', '7')
        column.append(e)
    elif 'BILBAO' in e:
        e =e.replace('BILBAO', '13')
        column.append(e)
    elif 'AVILÉS' in e:
        e =e.replace('AVILÉS', '5')
        column.append(e)
        
    
    elif 'Araba/Álava' in e:
        e =e.replace('Araba/Álava', '13')
        column.append(e)       
    elif 'Asturias' in e:
        e =e.replace('Asturias', '3')
        column.append(e)
    elif 'Ávila' in e:
        e =e.replace('Ávila', '5')
        column.append(e)
    elif 'Badajoz' in e:
        e =e.replace('Badajoz', '9')
        column.append(e)
    elif 'Barcelona' in e:
        e =e.replace('Barcelona', '7')
        column.append(e)
    elif 'Bizkaia' in e:
        e =e.replace('Bizkaia', '13')
        column.append(e)
    elif 'Burgos' in e:
        e =e.replace('Burgos', '5')
        column.append(e)
    elif 'Cáceres' in e:
        e =e.replace('Cáceres', '9')
        column.append(e)
    elif 'Jaén' in e:
        e =e.replace('Jaén', '1')
        column.append(e)
    elif 'Cádiz' in e:
        e =e.replace('Cádiz', '1')
        column.append(e)
    elif 'Cantabria' in e:
        e =e.replace('Cantabria', '4')
        column.append(e)
    elif 'Castellón/Castelló' in e:
        e =e.replace('Castellón/Castelló', '8')
        column.append(e)
    elif 'Ciudad Real' in e:
        e =e.replace('Ciudad Real', '6')
        column.append(e)
    elif 'Córdoba' in e:
        e =e.replace('Córdoba', '1')
        column.append(e)
    elif 'Coruña, A' in e:
        e =e.replace('Coruña, A', '10')
        column.append(e)
    elif 'A Coruña' in e:
        e =e.replace('A Coruña', '10')
        column.append(e)
    elif 'Cuenca' in e:
        e =e.replace('Cuenca', '6')
        column.append(e)
    elif 'Girona' in e:
        e =e.replace('Girona', '7')
        column.append(e)
    elif 'Gipuzkoa' in e:
        e =e.replace('Gipuzkoa', '13')
        column.append(e)
    elif 'Granada' in e:
        e =e.replace('Granada', '1')
        column.append(e)
    elif 'Guadalajara' in e:
        e =e.replace('Guadalajara', '6')
        column.append(e)
    elif 'Huelva' in e:
        e =e.replace('Huelva', '1')
        column.append(e)
    elif 'Huesca' in e:
        e =e.replace('Huesca', '2')
        column.append(e)
    elif 'Jaén' in e:
        e =e.replace('Jaén', '1')
        column.append(e)
    elif 'León' in e:
        e =e.replace('León', '5')
        column.append(e)
    elif 'Lleida' in e:
        e =e.replace('Lleida', '7 ')
        column.append(e)
    elif 'Lugo' in e:
        e =e.replace('Lugo', '10')
        column.append(e)
    elif 'Madrid' in e:
        e =e.replace('Madrid', '11')
        column.append(e)
    elif 'MADRID' in e:
        e =e.replace('MADRID', '11')
        column.append(e)
    elif 'Málaga' in e:
        e =e.replace('Málaga', '1')
        column.append(e)
    elif 'malaga' in e:
        e =e.replace('malaga', '1')
        column.append(e)
    elif 'MALAGA' in e:
        e =e.replace('MALAGA', '1')
        column.append(e)
    elif 'MÁLAGA' in e:
        e =e.replace('MÁLAGA', '1')
        column.append(e)
    elif 'ESTEPONA' in e:
        e =e.replace('ESTEPONA', '1')
        column.append(e)
    elif 'FUENGIROLA' in e:
        e =e.replace('FUENGIROLA', '1')
        column.append(e)
    elif 'MARBELLA' in e:
        e =e.replace('MARBELLA', '1')
        column.append(e)
    
    elif 'Navarra' in e:
        e =e.replace('Navarra', '12')
        column.append(e)
    elif 'Ourense' in e:
        e =e.replace('Ourense', '10')
        column.append(e)
    elif 'Palencia' in e:
        e =e.replace('Palencia', '5')
        column.append(e)
    elif 'Pontevedra' in e:
        e =e.replace('Pontevedra', '10')
        column.append(e)
    elif 'Rioja, La' in e:
        e =e.replace('Rioja, La', '14')
        column.append(e)
    elif 'Salamanca' in e:
        e =e.replace('Salamanca', '5')
        column.append(e)
    elif 'Segovia' in e:
        e =e.replace('Segovia', '11')
        column.append(e)
    elif 'Sevilla' in e:
        e =e.replace('Sevilla', '1')
        column.append(e)
    elif 'Soria' in e:
        e =e.replace('Soria', '5')
        column.append(e)
    elif 'Tarragona' in e:
        e =e.replace('Tarragona', '7')
        column.append(e)
    elif 'Girona' in e:
        e =e.replace('Girona', '7')
        column.append(e)
    elif 'Teruel' in e:
        e =e.replace('Teruel', '2')
        column.append(e)
    elif 'Toledo' in e:
        e =e.replace('Toledo', '6')
        column.append(e)
    elif 'Valencia/València' in e:
        e =e.replace('Valencia/València', '8')
        column.append(e)
    elif 'VALENCIA' in e:
        e =e.replace('VALENCIA', '8')
        column.append(e)
    elif 'Valladolid' in e:
        e =e.replace('Valladolid', '5')
        column.append(e)
    elif 'VALLADOLID' in e:
        e =e.replace('VALLADOLID', '5')
        column.append(e)
    elif 'ZAMORA' in e:
        e =e.replace('ZAMORA', '5')
        column.append(e)
    elif 'Zamora' in e:
        e =e.replace('Zamora', '5')
        column.append(e)
    elif 'Zaragoza' in e:
        e =e.replace('Zaragoza', '2')
        column.append(e)
    else:
        e=e.replace(e,'0')
        column.append(e)
        
    
    

