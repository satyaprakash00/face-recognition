
    df = pd.read_csv(csv_path)
    if df.empty:
        st.warning("Attendance file is empty.")
    else:
        try:
            styled_df = df.style.highlight_max(axis=0)
            st.write(styled_df.to_html(), unsafe_allow_html=True)
        except Exception as e:
            st.write("Could not display styled DataFrame:", e)
            st.dataframe(df)
except FileNotFoundError:
    st.error(f"Attendance file not found: {csv_path}")
except Exception as e:
    st.error(f"Error reading attendance file: {e}")