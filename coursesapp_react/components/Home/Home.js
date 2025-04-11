import { Text, View } from "react-native"
import globelStyles from "../../styles/globelStyles"
import { useEffect, useState } from "react"
import Apis, { endpoints } from "../../configs/Apis"
import { Chip } from "react-native-paper"

export default Home = () => {
    const [categories, setCategories] = useState([]);

    const loadCategories = async () => {
        let response = await Apis.get(endpoints['categories'])
        setCategories(response.data)
    }

    useEffect(() => {
        loadCategories();
    }, [])

    return (
        <View style={globelStyles.container}>
            <Text style={globelStyles.subject}>
                Quản lý khóa học
            </Text>

            <View style={[globelStyles.row, globelStyles.wrap]}>
                {categories.map(c => <Chip style={globelStyles.m} icon="label" key={c.id}>{c.name}</Chip>)}
            </View>
        </View>
    )
}