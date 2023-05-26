<template>
  <Toast
    class="app-toast"
    :closable="false"
    :position="position"
  >
    <template
      v-slot:message="{ message }"
    >
      <div
        v-if="message.src"
        class="app-toast__left mr-10"
      >
        <img
          class="app-toast__icon"
          alt="icon"
          :src="message.src"
        >
      </div>
      <div class="app-toast__right">
        <div class="app-toast__summary fw-7 fs-20 mb-5 fs-18-mb">
          {{ message.summary }}
        </div>
        <div class="app-toast__detail fs-16-mb">
          {{ message.detail }}
        </div>
      </div>
    </template>
  </Toast>
</template>

<script>
export default {
  name: 'AppToast',
  props: {
    position: {
      type: String,
      default: 'bottom-right',
    }
  },
  data: () => ({
  }),
  computed: {},
  methods: {},

}
</script>

<style lang="scss">
.app-toast {
  &__icon {
    width: 6rem;
    height: 6rem;
  }
  &.p-toast {
    opacity: 0.95;
    width: 50rem;
    bottom: 2rem;
    right: 2rem;
    @media (max-width: 600px) {
      width: auto;
      right: 2rem;
      bottom: .5rem;
    }
  }
  .p-toast-message {
    margin: 0 0 1rem 0;
    box-shadow: 0 .2rem 1.2rem 0 rgba(0, 0, 0, 0.1);
    border-radius: .6rem;
    &-error {
      background: #ffe7e6;
      border: solid #ff5757;
      border-width: 0 0 0 6px;
      color: #ff5757;
    }
  }
  .p-toast-message-content {
    padding: 1rem;
    border-width: 0 0 0 .6rem;
    display: flex;
    align-items: center;
    overflow: hidden;
  }
  .app-toast__right {
    flex: 1;
    overflow: hidden;
    max-height: 80vh;
    display: flex;
    flex-direction: column;
  }
  .p-toast-icon-close {
    align-self: flex-start;
  }
  .app-toast__detail {
    flex: 1;
  }
}

.p-toast {
  opacity: 0.9;
}
.p-toast .p-toast-message {
  margin: 0 0 1rem 0;
  box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.2), 0 4px 5px 0 rgba(0, 0, 0, 0.14), 0 1px 10px 0 rgba(0, 0, 0, 0.12);
  border-radius: 3px;
}
.p-toast .p-toast-message .p-toast-message-content {
  padding: 1rem;
  border-width: 0 0 0 6px;
}
.p-toast .p-toast-message .p-toast-message-content .p-toast-message-text {
  margin: 0 0 0 1rem;
}
.p-toast .p-toast-message .p-toast-message-content .p-toast-message-icon {
  font-size: 2rem;
}
.p-toast .p-toast-message .p-toast-message-content .p-toast-summary {
  font-weight: 700;
}
.p-toast .p-toast-message .p-toast-message-content .p-toast-detail {
  margin: 0.5rem 0 0 0;
}
.p-toast .p-toast-message .p-toast-icon-close {
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  background: transparent;
  transition: background-color 0.2s, color 0.2s, box-shadow 0.2s;
}
.p-toast .p-toast-message .p-toast-icon-close:hover {
  background: rgba(255, 255, 255, 0.3);
}
.p-toast .p-toast-message .p-toast-icon-close:focus {
  outline: 0 none;
  outline-offset: 0;
  box-shadow: 0 0 0 0.2rem #a6d5fa;
}
.p-toast .p-toast-message.p-toast-message-info {
  background: #B3E5FC;
  border: solid #0891cf;
  border-width: 0 0 0 6px;
  color: #044868;
}
.p-toast .p-toast-message.p-toast-message-info .p-toast-message-icon,
.p-toast .p-toast-message.p-toast-message-info .p-toast-icon-close {
  color: #044868;
}
.p-toast .p-toast-message.p-toast-message-success {
  background: #C8E6C9;
  border: solid #5ed60d;
  border-width: 0 0 0 6px;
  color: #224a23;
}
.p-toast .p-toast-message.p-toast-message-success .p-toast-message-icon,
.p-toast .p-toast-message.p-toast-message-success .p-toast-icon-close {
  color: #224a23;
}
.p-toast .p-toast-message.p-toast-message-warn {
  background: #FFECB3;
  border: solid #d9a300;
  border-width: 0 0 0 6px;
  color: #6d5100;
}
.p-toast .p-toast-message.p-toast-message-warn .p-toast-message-icon,
.p-toast .p-toast-message.p-toast-message-warn .p-toast-icon-close {
  color: #6d5100;
}
.p-toast .p-toast-message.p-toast-message-error {
  background: #FFCDD2;
  border: solid #e60017;
  border-width: 0 0 0 6px;
  color: #73000c;
}
.p-toast .p-toast-message.p-toast-message-error .p-toast-message-icon,
.p-toast .p-toast-message.p-toast-message-error .p-toast-icon-close {
  color: #73000c;
}

</style>
