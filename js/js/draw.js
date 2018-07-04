
function draw_lines(vertices, count){
var vertex_buffer = gl.createBuffer();                            // Cria um objeto do tipo bufffer, vazio
  gl.bindBuffer(gl.ARRAY_BUFFER, vertex_buffer);                  // Associa o buffer ao tipo ARRAY_BUFFER
  gl.bufferData(gl.ARRAY_BUFFER,                                  // Insere os vértices no buffer
                new Float32Array(vertices), gl.STATIC_DRAW);
  var coord = gl.getAttribLocation(shaderProgram, "coordinates"); // Verifica onde estão as coordenadas
  gl.vertexAttribPointer(coord, 3, gl.FLOAT, false, 0, 0);        // Point an attribute to the currently bound VBO
  gl.enableVertexAttribArray(coord);                              // Enable the attribute  
  gl.drawArrays(gl.LINE_STRIP, 0, count);                         // Desenha o objeto 
}

/*=================== Shaders ====================*/
function initShaders(){
  // Vertex shader source code
  var vertCode =
  'attribute vec3 coordinates;' +
  'void main(void) {' +
  ' gl_Position = vec4(coordinates, 1.0);' +
  '}';
  // Create a vertex shader object
  var vertShader = gl.createShader(gl.VERTEX_SHADER);
  // Attach vertex shader source code
  gl.shaderSource(vertShader, vertCode);
  // Compile the vertex shader
  gl.compileShader(vertShader);
  // Fragment shader source code
  var fragCode =
  'void main(void) {' +
  'gl_FragColor = vec4(0.0, 0.0, 0.0, 0.1);' +
  '}';
  // Create fragment shader object
  var fragShader = gl.createShader(gl.FRAGMENT_SHADER);
  // Attach fragment shader source code
  gl.shaderSource(fragShader, fragCode);
  // Compile the fragmentt shader
  gl.compileShader(fragShader);
  // Create a shader program object to store
  // the combined shader program
  shaderProgram = gl.createProgram();
  // Attach a vertex shader
  gl.attachShader(shaderProgram, vertShader);
  // Attach a fragment shader
  gl.attachShader(shaderProgram, fragShader);
  // Link both the programs
  gl.linkProgram(shaderProgram);
  // Use the combined shader program object
  gl.useProgram(shaderProgram);
}

function initWebGL(){
  canvas = document.querySelector("#glCanvas");                   // Inicializa o canvas (objeto HTML na página)
  gl = canvas.getContext("webgl");                                // Inicializa o contexto GL
  if (!gl) {                                                      // Só continua se o WebGL estiver disponível e funcionando
    alert("Este navegador não suporta WebGL.");
    return;
  }
  gl.clearColor(0.0, 0.5, 0.0, 1.0);                              // Define a cor de fundo do canvas
  gl.clear(gl.COLOR_BUFFER_BIT);                                  // Limpa o buffer de cores com uma cor específica
  initShaders();                                                  // Inicializa os shaders
  var vertices = [
    -0.7,-0.1,0,
    -0.3,0.6,0,
    -0.3,-0.3,0,
    0.2,0.6,0,
    0.3,-0.3,0,
    0.7,0.6,0 
  ]
  draw_lines(vertices, 6);
  // Set the view port
  // gl.viewport(0,0,canvas.width,canvas.height);
}