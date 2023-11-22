import goofpy

p = goofpy.Physics(0.0, 0.0, 50.0, 0.2, 127000, 1, 0, 0, 0, 10)
data = []
i = 0
while True:
    data.append(f'"id":"frame{i}","zpos":{p.z},"bounce":{p.b}')
    print(f"Updating physics frame {i}")
    goofpy.updatePhysics()
    i += 1

    if p.z == 0 and p.b == 0:
        data.append(f'"id":"frame{i}","zpos":{p.z},"bounce":{p.b}')
        break

goofpy.savePhysicsToJson(data)
