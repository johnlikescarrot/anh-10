#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Tai 05 giong doc neural Piper (chat luong medium, 22.05 kHz) hoan toan
# offline tu cac GitHub repository co chua ONNX blob THAT (khong dung Git LFS,
# vi mo hinh thuc thi chi cho phep github.com / pypi.org).
#
# Cach dung:  bash scripts/tts/download_models.sh
# Ket qua:     .tts-models/voices/<ten-giong>.onnx(+.json)
#
# Nguon model (ban quyen theo giay phep cua tung model Piper goc, phuc vu
# muc dich giao duc phi thuong mai):
#   - en_US-lessac-medium      : The-School-of-AI/Arcturus
#   - en_US-hfc_female-medium  : heyseth/Piper_TTS
#   - en_GB-jenny_dioco-medium : beneadie/Piper_TTS_API
#   - en_US-ryan-medium        : ThisIsRahmat/mvp-emmy
#   - en_GB-alan-medium        : ThisIsRahmat/mvp-emmy
# Runtime Piper duoc cai qua PyPI:  pip install piper-tts==1.2.0 onnxruntime
# ---------------------------------------------------------------------------
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
MODELS_DIR="$ROOT/.tts-models"
REPOS_DIR="$MODELS_DIR/_repos"
VOICES_DIR="$MODELS_DIR/voices"
mkdir -p "$REPOS_DIR" "$VOICES_DIR"

clone_sparse() {
  local url="$1" dir="$2" path="$3"
  if [[ ! -d "$REPOS_DIR/$dir/.git" ]]; then
    git clone --depth 1 --filter=blob:none --sparse "$url" "$REPOS_DIR/$dir"
  fi
  git -C "$REPOS_DIR/$dir" sparse-checkout set "$path"
}

# 1) en_US-lessac-medium (giong nu Anh-My)
clone_sparse https://github.com/The-School-of-AI/Arcturus.git \
  arcturus voice/piper_models
cp "$REPOS_DIR/arcturus/voice/piper_models/en_US-lessac-medium.onnx" \
   "$REPOS_DIR/arcturus/voice/piper_models/en_US-lessac-medium.onnx.json" "$VOICES_DIR/"

# 2) en_US-hfc_female-medium (giong nu Anh-My, am sac tre hon)
clone_sparse https://github.com/heyseth/Piper_TTS.git \
  heyseth voices
cp "$REPOS_DIR/heyseth/voices/en_US-hfc_female-medium.onnx" \
   "$REPOS_DIR/heyseth/voices/en_US-hfc_female-medium.onnx.json" "$VOICES_DIR/"

# 3) en_GB-jenny_dioco-medium (giong nu Anh-Anh)
clone_sparse https://github.com/beneadie/Piper_TTS_API.git \
  beneadie APIproj/piper/models
cp "$REPOS_DIR/beneadie/APIproj/piper/models/en_GB-jenny_dioco-medium.onnx" "$VOICES_DIR/"
cp "$REPOS_DIR/beneadie/APIproj/piper/models/en_en_GB_jenny_dioco_medium_en_GB-jenny_dioco-medium.onnx.json" \
   "$VOICES_DIR/en_GB-jenny_dioco-medium.onnx.json"

# 4-5) en_US-ryan-medium (nam Anh-My) & en_GB-alan-medium (nam Anh-Anh)
clone_sparse https://github.com/ThisIsRahmat/mvp-emmy.git \
  mvp backend/models/piper
for v in en_US-ryan-medium en_GB-alan-medium; do
  cp "$REPOS_DIR/mvp/backend/models/piper/$v.onnx" \
     "$REPOS_DIR/mvp/backend/models/piper/$v.onnx.json" "$VOICES_DIR/"
done

echo "Hoan tat. Giong doc co trong: $VOICES_DIR"
ls -lh "$VOICES_DIR"
