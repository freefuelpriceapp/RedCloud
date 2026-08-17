/**
 * RedCloud Dashboard UI Controller v2.1.0-Core
 * Handles local client-side interaction, drag-and-drop triggers,
 * and visual simulation of the (50, 20) Reed-Solomon Erasure Coding matrix.
 */

document.addEventListener("DOMContentLoaded", () => {
    const dropzone = document.querySelector(".dropzone");
    const shardBlocks = document.querySelectorAll(".shard-block");

    if (!dropzone) return;

    // Prevent default browser behavior for file drops
    ["dragenter", "dragover", "dragleave", "drop"].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => e.preventDefault(), false);
    });

    // Highlight dropzone on drag over
    ["dragenter", "dragover"].forEach(eventName => {
        dropzone.addEventListener(eventName, () => {
            dropzone.style.background = "rgba(255, 51, 51, 0.08)";
            dropzone.style.borderColor = "#ff6666";
        });
    });

    ["dragleave", "drop"].forEach(eventName => {
        dropzone.addEventListener(eventName, () => {
            dropzone.style.background = "rgba(255, 51, 51, 0.02)";
            dropzone.style.borderColor = "var(--accent-red)";
        });
    });

    // Handle the visual file drop event simulation
    dropzone.addEventListener("drop", (e) => {
        const files = e.dataTransfer.files;
        if (files.length === 0) return;

        const targetFile = files[0];
        console.log(`[UI Core] Ingested raw file: ${targetFile.name} (${targetFile.size} bytes)`);
        
        // Update drag zone text to mimic encryption phase
        dropzone.querySelector("p").innerText = "🔐 Encrypting & Sharding File...";
        
        // Reset all grid block visuals to blank states for animation sequencing
        shardBlocks.forEach(block => {
            block.style.opacity = "0.2";
            block.style.transform = "scale(0.8)";
        });

        // Cascade animation simulating client-side mathematical block serialization
        shardBlocks.forEach((block, index) => {
            setTimeout(() => {
                block.style.opacity = "1";
                block.style.transform = "scale(1)";
                block.style.transition = "all 0.15s ease-out";
                
                // Play subtle sound click or log matrix coordinate tracking
                if (index === shardBlocks.length - 1) {
                    dropzone.querySelector("p").innerText = "🔴 File Successfully Scattered!";
                    setTimeout(() => {
                        dropzone.querySelector("p").innerText = "Drag & Drop Files Here to Shard";
                    }, 3000);
                }
            }, index * 25); // Sequential block cascading effect
        });
    });
});
