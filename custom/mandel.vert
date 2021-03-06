//TODO: deleting unused in/out variables breaks this
in vec3 aVertexPosition;
in vec3 aVertexNormal;
in vec4 aVertexColour;
in vec2 aVertexTexCoord;
uniform mat4 uMVMatrix;
uniform mat4 uPMatrix;
uniform mat4 uNMatrix;

uniform vec4 uColour;

out vec4 vColour;
out vec3 vNormal;
out vec3 vPosEye;
out vec2 vTexCoord;
out vec3 vVertex;

void main(void) {
  vec4 coords = uMVMatrix * vec4(aVertexPosition.xy, 0.0, 1.0);
  vTexCoord = aVertexTexCoord;  
  vec4 mvPosition = uMVMatrix * vec4(aVertexPosition, 1.0);
  vPosEye = vec3(mvPosition);
  gl_Position = uPMatrix * mvPosition;

  vNormal = normalize(mat3(uNMatrix) * aVertexNormal);

  if (uColour.a > 0.0)
    vColour = uColour;
  else
    vColour = aVertexColour;

  vVertex = aVertexPosition;
}

