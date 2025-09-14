import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import { useRef } from "react";

function AnimatedCube() {
  const meshRef = useRef();

  useFrame((state, delta) => {
    const t = state.clock.getElapsedTime();

    // Trayectoria circular en XZ
    meshRef.current.position.x = Math.sin(t) * 2;
    meshRef.current.position.z = Math.cos(t) * 2;

    // Rotación continua
    meshRef.current.rotation.x += delta;
    meshRef.current.rotation.y += delta * 1.2;

    // Escala pulsante
    const scale = 1 + 0.3 * Math.sin(t * 2);
    meshRef.current.scale.set(scale, scale, scale);
  });

  return (
    <mesh ref={meshRef}>
      <boxGeometry args={[1, 1, 1]} /> 
      <meshStandardMaterial color="royalblue" />
    </mesh>
  );
}

export default function App() {
  return (
    <Canvas camera={{ position: [5, 5, 5] }}>
      {/* Luz ambiental y direccional */}
      <ambientLight intensity={0.5} />
      <directionalLight position={[5, 5, 5]} intensity={1} />

      {/* Nuestro cubo animado */}
      <AnimatedCube />

      {/* Bonus: controles de cámara */}
      <OrbitControls />
    </Canvas>
  );
}
