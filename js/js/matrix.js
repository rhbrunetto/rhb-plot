export function loadIdentity(n) {
  mvMatrix = Matrix.I(n);
}

export function multMatrix(m) {
  mvMatrix = mvMatrix.x(m);
}

export function mvTranslate(v) {
  multMatrix(Matrix.Translation($V([v[0], v[1], v[2]])).ensure4x4());
}

export function setMatrixUniforms(gl, perspectiveMatrix) {
  var pUniform = gl.getUniformLocation(shaderProgram, "uPMatrix");
  gl.uniformMatrix4fv(pUniform, false, new Float32Array(perspectiveMatrix.flatten()));

  var mvUniform = gl.getUniformLocation(shaderProgram, "uMVMatrix");
  gl.uniformMatrix4fv(mvUniform, false, new Float32Array(mvMatrix.flatten()));
}
